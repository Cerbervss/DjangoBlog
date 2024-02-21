from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titolo = models.CharField(max_length = 100)
    contenuto = models.TextField()
    data = models.DateTimeField(default = timezone.now)
    autore = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.titolo
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk" : self.pk})