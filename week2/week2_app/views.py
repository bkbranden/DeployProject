from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Subscription, Subscriber
from .forms import SubscriberForm

def get_subscriber(request):
    if(request.method == "POST"):
        form = SubscriberForm(request.POST)

        if form.is_valid():
            print("TESTING....")
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
            print(form.cleaned_data['email'])
            print("DONE TESTING...")
            return HttpResponseRedirect('/')

    else:
        form = SubscriberForm()
    
    return render(request, "index.html", {'form': form})

def index(request):
    return render(request, 'index.html')