from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError



def homeView(request: HttpRequest):
    return render(request, 'HoosExchangeSite/home.html')

def makePost(request: HttpRequest):
    return render(request, 'HoosExchangeSite/makePost.html')

def viewItems(request: HttpRequest):
    return render(request, 'HoosExchangeSite/viewItems.html')

