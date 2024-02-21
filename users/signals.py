from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profilo

@receiver(post_save, sender = User)
def crea_profilo(sender, instance, created, **kwargs):
    if(created):
        profilo.objects.create(user = instance)
    
@receiver(post_save, sender = User)
def salva_profilo(sender, instance, **kwargs):
    instance.profilo.save()
    