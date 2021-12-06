from django.shortcuts import render , redirect

def home(request):
    return render(request,'adminhome.html')

def category(request):
    return render(request,'category.html')    

def product(request):
    return render(request,'product.html')

def logout(request):
    return redirect("/alogin")
