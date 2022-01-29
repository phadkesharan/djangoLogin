from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signUpRedirect(request):
    
    user = request.POST['User']

    if user == None:
        return redirect('home')

    return render(request, 'signUp.html', {'typeOfUser': user})

def signUp(request):

    if request.POST:
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        image = request.POST['dp']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        passwordverify = request.POST['confirm']
        type = request.POST['type']

        user = User(
            firstName=firstname,
            lastName=lastname,
            username=username,
            profilePicture=image,
            emailId=email,
            address=address,
            password=password,
            user=type,
            confirmPassword=passwordverify,
        )

        if len(User.objects.filter(username=username)) > 1:
            messages.error(request, "Username already exists!! Use other Username")
            user.delete()
            return redirect("home")

        if password != passwordverify:
            messages.error(request, 'password and confirm password do not match')
            user.delete()
            return redirect('home')

        user.save()

    messages.info(request, 'Accout Created Successfully!!')
    return render(request, 'login.html')


def login(request):

    if request.POST:

        username = request.POST['username']
        password = request.POST['password']


        if len(User.objects.filter(username=username)) == 1:
            user = User.objects.filter(username=username)[0]
            print("user valid")
            print(user)
            fname = user.firstName
            lname = user.lastName
            type = user.user
            messages.success(request, "Login Successfull!!")
            return render(request, "dashBoard.html", context={'firstname': fname, 'lastname': lname, 'type': type})

        else:
            print("user not valid")
            messages.error(request, "Bad Credentials")
            return redirect("home")

    return render(request, 'login.html')

