from django import forms
from django.forms import Form
from django.core.mail import send_mail
from itc.settings import EMAIL_HOST_USER

class ContactForm (Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'id' : 'firstName', 'placeholder' : 'Name *', 'style' : 'width: 22vw; padding: 16px; margin-top: 10px;'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'id' : 'email', 'placeholder' : 'Email *', 'style' : 'width: 22vw; padding: 16px; margin-top: 10px;'}) )
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'id' : 'message', 'placeholder' : 'Message *', 'style' : 'width: 45vw;'}))

    def send_email(self):
        clean_data = self.cleaned_data
        send_mail(
            subject=f"Email from {clean_data.get('first_name')} ({clean_data.get('email')})",
            message=clean_data.get('comment'),
            from_email=EMAIL_HOST_USER,
            recipient_list=[EMAIL_HOST_USER]
        )