from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('services/', views.ServiceView.as_view(), name="services"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('thanks/', views.ThanksView.as_view(), name="thanks")
]