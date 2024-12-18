from django.shortcuts import render, redirect
from . models import Listing
from .forms import ListingForm


# Create your views here.

# CRUD - create, retrieve, update, delete, list


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }    
    return render(request, 'listings/listing.html', context)


def listing_create(request):
    form = ListingForm() # create an empty form, which is a get request.
    
    # what happen if the request is POST:
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {
        'form': form
    }
    return render(request, 'listings/listing_create.html', context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing) # create a form with the data from the database.
    
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'listings/listing_update.html', context)


def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    print('Your deletion was susccefully!')
    return redirect('/')