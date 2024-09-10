from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from cart.cart import Cart

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username= request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)
            messages.success(request,("You have been logged in!!!"))
            return redirect('home')
        else:
            messages.error(request,("Error logging in!!!"))
            return redirect('login')
    else:    
        return render(request,'login.html',{})

    
def register_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        #Check if password and confirm_password is same or not
        if password != confirm_password:
            messages.warning(request, "Password and Confirm Password does not match")
            return redirect('register')

        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            messages.warning(request, "User already exists")
            return redirect('register')


        # If the user doesn't exist, proceed with creating a new user
        my_user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
        my_user.set_password(password)
        try:
            my_user.save()
            login(request, my_user)   #This will directly log the user immediately after registering.
            messages.success(request, "You have been registered successfully!!!")
            return redirect('update_info')
        except:
            messages.error(request, "Error while registering!!!")

    return render(request, 'register.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out!!!"))
    return redirect('home')

@login_required(login_url='login')
def view_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name= request.POST.get('first_name')
        user.last_name= request.POST.get('last_name')
        user.email= request.POST.get('email')
        user.save()
        messages.success(request,("Your profile have been updated successfully!!!"))
        return redirect('view_profile')
    return render(request, 'edit_profile.html', {'user': user})

@login_required(login_url='login')
def delete_profile(request):
    user = request.user
    if request.method=='POST':
        user.delete()
        messages.error(request,("Your profile have been deleted successfully!!!"))
        return redirect('home')
    return render(request, 'delete_profile.html', {'user': user})


@login_required
def update_info(request):
    if request.method == "POST":
        profile = Profile.objects.get(user__id=request.user.id)
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('home')
    else:
        profile = Profile.objects.get(user=request.user)
    
    return render(request, 'info.html', {'profile': profile})