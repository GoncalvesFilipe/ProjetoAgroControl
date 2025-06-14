"""
URL configuration for AgroControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index
from app import views 
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def redirect_inicio(request):
    return redirect('inicio')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
    path('animais/', views.lista_animais, name='lista_animais'),
    path('animais/<int:pk>/', views.detalhe_animal, name='detalhe_animal'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('movimentos/', views.lista_movimentos, name='lista_movimentos'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inicio/', views.index, name='inicio'),
    path('início/', redirect_inicio),  # redireciona /início/ para /inicio/
]
