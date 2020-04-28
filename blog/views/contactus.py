from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from ..models import Posts,PostDetail,About,Comment
from django.conf import settings
import json
from ..errorMessage import getApiMsg
import re 
from ..utility import utils

# Create your views here.

def saveContact(request):
   return render(request, 'contactus.html', {})
        
