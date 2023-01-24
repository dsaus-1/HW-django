from catalog.models import Product, Blog
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse


def contacts(request):
    if request.method == 'POST':
        print(f"Name: {request.POST.get('name')}")
        print(f"Phone: {request.POST.get('phone')}")
        print(f"Message: {request.POST.get('message')}")
    return render(request, 'catalog/contact.html')


class ProductListView(ListView):
    model = Product

class BlogListView(ListView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'content', 'image_preview')
    success_url = reverse_lazy('catalog:blog')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'image_preview')

    def get_success_url(self):
        slug = self.kwargs["slug"]
        return reverse("catalog:detail", kwargs={"slug": slug})

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_of_views += 1
        obj.save()

        return obj



