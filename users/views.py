from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import PasswordChangeForm

from blog.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfiloUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect("blog-home")
    logout(request)
    messages.add_message(request, messages.INFO, 'Hai effettuato il logout')
    return redirect("blog-home")

def register(request):
    if request.user.is_authenticated:
        return redirect("blog-home")
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username.capitalize()}, il tuo account è stato creato!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form, "title": "Registrati"})

def profile_guest(request, utente):
    user1 = User.objects.filter(username = utente).first()
    count = Post.objects.filter(autore = user1).count()
    if not user1:
        return render(request, "users/404.html")
    return render(request, "users/profile_guest.html", {"utente": user1, "count": count, "title": user1.username})

@login_required
def profile(request):
    return render(request, "users/profile.html", {"count": Post.objects.filter(autore = request.user).count(), "title": request.user.username})

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfiloUpdateForm(request.POST, request.FILES, instance = request.user.profilo)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Il tuo account è stato modificato!")
            return redirect ("profile")
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfiloUpdateForm(instance = request.user.profilo)
    context = {
        "u_form": u_form,
        "p_form": p_form,
        "title": request.user.username
    }

    return render(request, "users/update_profile.html", context)

@login_required
def update_password(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(user = request.user, data = request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request, f"La tua password è stata modificata!")
            return redirect ("profile")
    else:
        pass_form = PasswordChangeForm(user = request.user)
    context = {
        "pass_form": pass_form,
        "title": request.user.username
    }

    return render(request, "users/update_password.html", context)


