from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=15, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# REQUIRED_FIELDS deve conter todos os campos do seu modelo,
# mas não precisa inserir o USERNAME_FIELD ou password pois
# estes campos sempre serão usados.

# Com esta alteração podemos logar nosso usuário com email.