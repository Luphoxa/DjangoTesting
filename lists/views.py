# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text']) # creating a new Item without needing save()
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
