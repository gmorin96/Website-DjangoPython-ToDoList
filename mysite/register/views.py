from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})

def log_out(response):
    print(response.method)
    if response.method == "POST":
        return render(response, "register/log_out.html",{})