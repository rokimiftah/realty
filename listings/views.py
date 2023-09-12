from django.shortcuts import render

from .models import Listing


# Create your views here.
def get_all_listings(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(
        request,
        "listings/index.html",
        context,
    )
