from django.shortcuts import render
from card.models import card
from django.core.paginator import Paginator
def home(request):
    car_var = card.objects.all()
    pagination = Paginator(car_var,2)
    page_number = request.GET.get('page')
    servicedatafinal = pagination.get_page(page_number)
    
    data = {
        'dt':car_var,
        'servicedata':servicedatafinal,
    }
    return render (request , 'home.html',data)