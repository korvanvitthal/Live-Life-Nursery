from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request,'home.html',context)

def nursery(request):
    return render(request,'nursery.html')

def gallery(request):
    return render(request,'gallery.html')