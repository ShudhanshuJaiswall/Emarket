from django.urls import path 
from . import views

urlpatterns = [
    path('home',views.home),
    path('category',views.category),
    path('product',views.product),
    path('logout',views.logout),

]
