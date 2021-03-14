from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView
from framework.forms import ContactForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "framework/index.html"


class ServiceView(TemplateView):
    template_name = "framework/services.html"


class ContactView(FormView):
    template_name = "framework/index.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class ThanksView(View):
    def get(self,request):
        return HttpResponse("Thanks!")

    def post(self,request):
        return HttpResponse("Thanks!")