from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger , Paginator
from .choices import price_choices ,bedroom_choices , state_choices 


# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Listing




def index(request):
  listings = Listing.objects.order_by('-last_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)





def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    
    context = {
        'listing':listing,
    }
    return render(request,"listings/listing.html",context)




def search(request):
    querryset_list = Listing.objects.order_by('-last_date')
    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querryset_list = querryset_list.filter(description__icontains = keywords)
        

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querryset_list = querryset_list.filter(city__iexact = city)
        

    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querryset_list = querryset_list.filter(state__iexact = state)
        

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querryset_list = querryset_list.filter(bedrooms__lte = bedrooms)
        
    
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querryset_list = querryset_list.filter(price__lte = price)
        
    
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':querryset_list,
        'values': request.GET
    }

    return render(request,"listings/search.html",context)
