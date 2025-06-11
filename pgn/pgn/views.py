from django.shortcuts import render
from card.models import card
from django.core.paginator import Paginator
from fm.models import forms
from django.core.mail import send_mail


def home(request):
    car_var = card.objects.all()
    pagination = Paginator(car_var,2)
    page_number = request.GET.get('page')
    servicedatafinal = pagination.get_page(page_number)
    
    data = {
        'dt':car_var,
        'servicedata':servicedatafinal,
    }
    if request.method == 'POST':
        nam = request.POST.get('name1')
        emai = request.POST.get('name')
        numb = request.POST.get('number')
        messa = request.POST.get('message')
        en = forms(user_name = nam ,user_email = emai ,user_phone=numb,user_message=messa )
        en.save()
        subject = f' New form submission from {nam}'
        user_email_1=emai
        phone_number=numb
        messages= f'{nam} Thanks for Submission the form your Phone number is {phone_number} and email is {user_email_1}'
        send_mail(
        subject,
        messages,
        'pellowdeveloper@gmail.com',
        [user_email_1],
        fail_silently=False,
        )

    return render (request , 'home.html',data)

def formss(request):
    if request.method == 'POST':
        nam = request.POST.get('name1')
        emai = request.POST.get('name')
        numb = request.POST.get('number')
        messa = request.POST.get('message')
        en = forms(user_name = nam ,user_email = emai ,user_phone=numb,user_message=messa )
        en.save()

    return render(request, 'home.html')
