from django.db import models
from datetime import date, timedelta, datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class Book(models.Model):
    Author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    BookName = models.CharField(max_length=30)
    Context = models.CharField(max_length=800)
    Editorial = models.CharField(max_length=30)
    Paginas = models.CharField(max_length=4)
    Picture  = models.CharField(max_length=800)
    Date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.BookName
