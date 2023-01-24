from catalog.views import ProductListView, contacts, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView
from django.urls import path
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),

]
