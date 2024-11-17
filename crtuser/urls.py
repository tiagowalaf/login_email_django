from django.urls import path
from .views import HomeCreateUser, ValidateCrtUser

app_name = "create"
urlpatterns = [
    path('', HomeCreateUser, name="home_create_user"),
    path('validate/', ValidateCrtUser, name="validate_crt"),
]