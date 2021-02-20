from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "framework/homepage.html"


class ServiceView(TemplateView):
    template_name = "framework/services.html"


class ContactView(TemplateView):
    template_name = "framework/contact.html"

