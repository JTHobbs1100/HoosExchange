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

from .models import Listing
from .forms import makeListingForm


def homeView(request: HttpRequest):
    return render(request, 'HoosExchangeSite/home.html')

def makePost(request: HttpRequest):
    name = "BAD"


    if request.method == 'POST':

        form = makeListingForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

    else:
        form = makeListingForm()





    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'HoosExchangeSite/makePost.html', context)

class viewItems(generic.ListView):
    template_name = 'HoosExchangeSite/viewItems.html'
    context_object_name = 'listings_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Listing.objects.all()
