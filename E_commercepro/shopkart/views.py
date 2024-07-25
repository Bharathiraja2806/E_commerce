from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return render(request, 'shop/index.html')

def register(request):
    return render(request, 'shop/register.html')

def collections(request):
    Category = category.objects.filter(status=0)    
    return render(request, 'shop/collections.html',{'category':Category})

def collectionsview(request, name):
    if(category.objects.filter(name=name , status=0)) :
        products = Product.objects.filter(category__name = name) 
        return render(request, 'shop/products/index.html',{'products':products, 'category_name': name})
    else:
        messages.warning(request, "NO Such Products Found")
        return redirect('collections')

def product_details(request, cname,pname):
    if (category.objects.filter(name = cname, status = 0)):
       if (Product.objects.filter(name = pname, status = 0)):
           products = Product.objects.filter(name = pname, status = 0).first()
           return render(request, 'shop/products/product_details.html',{"products":products})
       else:
           messages.error(request,"NO such product found")
           return redirect('collections')
    else:
        messages.error(request,"NO such category found")
        return redirect('collections')    