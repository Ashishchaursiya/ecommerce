from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('category/', views.Category,name="category"),
    path('search/', views.search,name="search"),
    path('product/<int:id>',views.product,name='product'),
    path('checkout/<int:id>',views.checkout,name='checkout'),
    path('tracker',views.tracker,name='tracker'),
    path('cart_checkout',views.cart_checkout,name="cart_checkout")


    
   
]  