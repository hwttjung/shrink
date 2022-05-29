from django.shortcuts import render, redirect
from shorten.models import User
# Create your views here.

def index(request) :
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anoymous User!"
    print(email)
    if request.user.is_authenticated is False:
        email = "Anonymous User"
    print(email)
    return render(request, "base.html", {"welcome_msg": f"Hello {email}"})


def redirect_test(request) :
    print("Go Redirect!")
    return redirect("index")