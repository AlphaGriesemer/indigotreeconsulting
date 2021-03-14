from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactView.as_view(), name="index"),
    path('thanks/', views.ThanksView.as_view(), name="thanks")
]