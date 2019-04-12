from django.shortcuts import render,get_object_or_404
from listings.models import Listing
from django.core.paginator import Paginator
from listings.choice import bedroomChoices,stateChoices,priceChoices
# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('listDate').filter(isPublished=True)
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    listings = paginator.get_page(page)
    context = {
        "listings":listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listingId):
    listing = get_object_or_404(Listing,pk=listingId)
    context = {
        "listing":listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query = Listing.objects.order_by("listDate")

    # For Searching In The Keyword
    if 'keywords' in request.GET:
        keyword = request.GET['keywords']
        if keyword:
            query = query.filter(description__icontains=keyword)

    # For Searching City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query = query.filter(city__iexact=city)

    # For Searching State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query = query.filter(state__iexact=state)
    
    # For Searching Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query = query.filter(bedrooms__lte=bedrooms)

    # For Searching Prices
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query = query.filter(price__lte=price)

    context = {
        'bedroomChoices':bedroomChoices,
        'stateChoices':stateChoices,
        'priceChoices':priceChoices,
        "listings":query
    }
    return render(request,'listings/search.html',context)