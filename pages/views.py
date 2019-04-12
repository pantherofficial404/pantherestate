from django.shortcuts import render
from listings.models import Listing
from realtor.models import Realtor
from listings.choice import bedroomChoices,priceChoices,stateChoices
# Create your views here.
def home(request):
    listings = Listing.objects.order_by('listDate').filter(isPublished=True)[:3]

    context = {
        "listings":listings,
        "bedroomChoices":bedroomChoices,
        "priceChoices":priceChoices,
        "stateChoices":stateChoices,
    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by("-hireDate")[:3]
    mvp = Realtor.objects.filter(isMVP=True)[:1]
    print(mvp)
    context = {
        "realtors":realtors,
        "mvp":mvp
    }
    return render(request,'pages/about.html',context)