from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),

    path('clogin',views.clogin),
    path('alogin',views.alogin),

    path('master/',include('master.urls'))
]
