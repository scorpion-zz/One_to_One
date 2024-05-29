from django.shortcuts import render

from glav.models import Land, Capital


def get_page_1(request):
    land = Land.objects.all()
    for i in land:
        print(i)
    context = {
        'land':land,
    }
    return render(request,'page_1.html',context)



def get_plus(request):
     return render(request,'plus.html')


def get_capitalize(request, id):
    cap =  Capital.objects.filter(land_id=id)
    land = Land.objects.all()
    context = {
        'cap':cap,
        'land':land,
    }
    return render(request, 'capitalize.html',context)