from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('photographers/', views.photographer_list, name='photographer_list'),
    path('photographers/<int:pk>', views.photographer_detail, name='photographer_detail'),
    path('photographers/new', views.photographer_create, name='photographer_create'),
    path('photographers/<int:pk>/edit', views.photographer_edit, name='photographer_edit'),
    path('photographers/<int:pk>/delete', views.photographer_delete, name='photographer_delete'),

    path('shoots/', views.shoot_list, name='shoot_list'),
    path('shoots/<int:pk>', views.shoot_detail, name='shoot_detail'),
    path('shoots/new', views.shoot_create, name='shoot_create'),
    path('shoots/<int:pk>/edit', views.shoot_edit, name='shoot_edit'),
    path('shoots/<int:pk>/delete', views.shoot_delete, name='shoot_delete'),
]

