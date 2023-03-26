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
import random

from .models import newModel
from .forms import makeListingForm


def homeView(request: HttpRequest):
    return render(request, 'HoosExchangeSite/home.html')

def makePost(request: HttpRequest):
    name = "BAD"
    img_object = "BADBADBAD"


    if request.method == 'POST':

        form = makeListingForm(request.POST, request.FILES)
        if form.is_valid():
            # personalKey = random.randint(1, 1000000000)
            form.save()
            img_object = form.instance
            #return HttpResponseRedirect(reverse('HoosExchangeSite:viewItems'))
    else:
        form = makeListingForm()
    context = {
        'form': form,
        'name': name,
        'img_obj': img_object,
    }

    return render(request, 'HoosExchangeSite/makePost.html', context)

def viewItems(request):

        Listings = newModel.objects.all()
        return render(request, 'HoosExchangeSite/viewItems.html',
                       {'listings_list': Listings})
def singleItem(request, id):
    singleListing= newModel.objects.get(id=id)
    lname = singleListing.name
    ltag = singleListing.tag
    ldescription = singleListing.description
    lprice = singleListing.price
    lphone = singleListing.phone_number
    lemail = singleListing.email
    limage = singleListing.image
    context={'lname':lname, 'ltag':ltag, 'ldescription':ldescription,'lprice':lprice, 'lphone':lphone, 'lemail':lemail, 'limage':limage}
    return render(request, 'HoosExchangeSite/singleItem.html', context)
