from django.urls import path
from . import views

urlpatterns = [
    path("<int:listingId>/",views.listing,name="listing"),
    path("",views.listings,name="listings"),
    path("search",views.search,name="search")
]