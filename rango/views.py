## -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunch, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse(
        '''
        <p>Rango says here is the about page.</p>
        <a href='/'>index</a>
        '''
    )