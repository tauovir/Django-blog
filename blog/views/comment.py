from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from ..models import Posts,PostDetail,About,Comment
from django.conf import settings
import json
from ..errorMessage import getApiMsg
import re 
from ..utility import utils

# Create your views here.

def saveComment(request):
    if request.method == 'POST' and request.user is not None:
        commentObject = Comment()
        commentObject.user = request.user
        commentObject.post_id = request.POST['post_id']
        commentObject.comment = request.POST['comment']
        commentObject.replied_on = request.POST['replyOn']
        commentObject.save()
        response = {'message' : "Thank you for your valuable comment",'code': 200, 'data': {}}
        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        response = {'message' : getApiMsg(201),'code': 201, 'data': {}}
        return HttpResponse(json.dumps(response), content_type="application/json")
        
