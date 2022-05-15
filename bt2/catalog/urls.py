from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('books/', views.BookListView.as_view(), name='books'),
    path('laptops/', views.LaptopListView.as_view(), name='laptops'),
    path('mobiles/', views.MobileListView.as_view(), name='mobiles'),
    path('clothes/', views.ClothListView.as_view(), name='clothes'),
    path('shoes/', views.ShoeListView.as_view(), name='shoes'),

    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('laptop/<int:pk>', views.LaptopDetailView.as_view(), name='laptop-detail'),
    path('mobile/<int:pk>', views.MobileDetailView.as_view(), name='mobile-detail'),
    path('cloth/<int:pk>', views.ClothDetailView.as_view(), name='cloth-detail'),
    path('shoe/<int:pk>', views.ShoeDetailView.as_view(), name='shoe-detail'),

    path('cart', views.get_cart, name='cart'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('edit-cart', views.edit_cart, name='edit-cart'),
    path('delete-cart', views.delete_cart, name='delete-cart'),
    path('buy', views.buy, name='buy'),
]
