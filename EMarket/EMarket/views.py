from django.shortcuts import render,redirect

def home(request):
    return render(request,'index.html')

def clogin(request):
        return render(request,'clogin.html')
def alogin(request):
    if request.method == "GET":
        return render(request,'alogin.html')
    else:
        email = request.POST.get('email')        
        password = request.POST.get('password')        
        if email=="admin@emarket.com" and password=="123":
            return redirect('/master/home')
        else:            
            return redirect('/alogin')