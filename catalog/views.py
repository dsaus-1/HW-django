from catalog.models import Product
from django.shortcuts import render

def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        print(f"Name: {request.POST.get('name')}")
        print(f"Phone: {request.POST.get('phone')}")
        print(f"Message: {request.POST.get('message')}")
    return render(request, 'catalog/contact.html')

def base(request):
    return render(request, 'catalog/base.html')