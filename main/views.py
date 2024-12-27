from django.shortcuts import render
from django.http import HttpResponse

def index(rerquest):
    context = {
        'title': 'Home',
        'content': 'Главаня страница магазина',

        'something': 'Some text that i will add laiter',
        'list':['first','second'],
        'dict':{'first':1, 'second':2},
        'loged_in': True,
    }
    return render(rerquest, 'main/index.html',context)

def about(request) -> HttpResponse:
    return HttpResponse('About Page')