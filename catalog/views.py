from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        print(f"Name: {request.POST.get('name')}")
        print(f"Phone: {request.POST.get('phone')}")
        print(f"Message: {request.POST.get('message')}")
    return render(request, 'catalog/contact.html')