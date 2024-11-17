from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', include('crtuser.urls')),
    path('admin/', admin.site.urls),
]