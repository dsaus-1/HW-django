from django.contrib.auth.decorators import login_required

from catalog.views import *
from django.urls import path
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('product_create/', login_required(ProductCreateView.as_view()), name='product_create'),
    path('product_update/<int:pk>/', login_required(ProductUpdateView.as_view()), name='product_update'),
    path('product_delete/<int:pk>/', login_required(ProductDeleteView.as_view()), name='product_delete'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('create/', login_required(BlogCreateView.as_view()), name='create'),
    path('update/<slug:slug>/', login_required(BlogUpdateView.as_view()), name='update'),
    path('delete/<slug:slug>/', login_required(BlogDeleteView.as_view()), name='delete'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),

]
