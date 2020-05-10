from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from ..models import Posts,PostDetail,About,Comment
from django.conf import settings
import json
from ..errorMessage import getApiMsg
import re 
from ..utility import utils
from blog.forms import ContactusForm
from blog.models import Contactus,About
from django.contrib import messages
# Create your views here.

def saveContact(request):

  aboutData = About.objects.first()
  if request.method == 'POST':
       # create a form instance and populate it with data from the request:
        form = ContactusForm(request.POST)
         # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #cleanedData = form.cleaned_data
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for contacting us')
            # redirect to a new URL:
            return redirect('contactus')
            #return render(request, 'contactus.html',{'aboutData' : aboutData} )
          # if a GET (or any other method) we'll create a blank form
  else:
        form = ContactusForm()

  return render(request, 'contactus.html', {'form': form,'aboutData' : aboutData})
  
  
  
   #return render(request, 'contactus-copy.html', {})
        
