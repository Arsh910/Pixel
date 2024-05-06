from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Team ,Bugs
from django import forms
from django.core.mail import send_mail
# Create your views here.

class Bugs_form(forms.Form):
    name=forms.CharField(max_length=20,label='Name',widget=forms.TextInput(attrs={'placeholder':'Name here','class':'input','id':'indfi-5'}))
    email=forms.EmailField(max_length=50,label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email here', 'class':"input",'id':"ijowk-7"}))
    message=forms.CharField(max_length=500,label='Message',widget=forms.Textarea(attrs={'placeholder':'type message here',"class":"textinput",'id':"i5vyy-7"}))

def team_view(requests):
    team=Team.objects.all()
    return render(requests,'home.html',{'data':team})

def Bugs_in(requests):
    if requests.method == 'POST':
        form = Bugs_form(requests.POST, requests.FILES)
        data = Bugs.objects.all()
        if form.is_valid():
            object = Bugs.objects.create(
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message'],
                author=requests.user
            )
            object.save()
            name='Thanks for Uploading'
            message = f"We truly appreciate your effort and dedication in helping us improve our website {form.cleaned_data['name']}. It's because of thoughtful individuals like you that we can continue to grow and deliver a better service. " \
                      f"Thank you for your contribution and for being an integral part of our community."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]
            send_mail(name, message, email_from, recipient_list)
            return render(requests, 'done.html',{'data':data})
        else:
            return render(requests, 'report_Bugss.html', {'form': form})
    else:
        return render(requests, 'report_Bugss.html', {'form': Bugs_form()})
