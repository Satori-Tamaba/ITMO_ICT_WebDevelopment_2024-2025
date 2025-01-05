from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('user/<slug:user_slug>/', views.show_user, name ='show_user'),
    path('driver/<slug:driver_slug>/', views.show_driver, name='show_driver'),
    path('race/<int:race_id>/', views.detail_race, name='detail_race'),
]
