from django.shortcuts import redirect, render
from matplotlib.style import context
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)  
        messages.success(request, 'Başarıyla kayıt oldun.')

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user1 = authenticate(username=username,password=password)
        
        if user1 is None:
            messages.info(request,"Böyle bir kullanıcı bulunmuyor.")
            return render(request,"login.html",context)
        
        messages.success(request,"Giriş yaptın.")
        login(request,user1)
        return redirect("index")
    
    return render(request,"login.html",context)
        

    return render(request,"login.html")

def logOut(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptın.")
    return redirect("index")
