from django.contrib import admin
from django.urls import path
from api.login.login_view import (login_view, register_view)
from api.home.home_views import home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),  # Ruta de login
    path('logout/', home_views, name='logout'),  # Ruta de logout
    path('', home_views, name='home'),  # Ruta de home (index)
    path('register/', register_view, name='register'),  # Ruta de registro de usuario

]

