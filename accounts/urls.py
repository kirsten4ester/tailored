# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# all socials:
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Login / Log Out
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logout'),
    # Sign Up
    path('accounts/signup', views.sign_up, name="signup"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
#     url(r'^settings/$', core_views.settings, name='settings'),
#     url(r'^settings/password/$', core_views.password, name='password'),
]