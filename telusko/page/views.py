from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        login_successful = False

        if user is not None:
            login_successful = True 
            login(request, user)
            return redirect('home')  # Replace 'success_url' with the URL you want to redirect to upon successful login.
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'login1.html')  # Replace 'login.html' with the actual login template.








def reg_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone_number = request.POST['number']
        
        # Create a new user instance and save it
        user = CustomUser.objects.create_user(email=email, password=password, name=name, phone_number=phone_number)
        
        # Log the user in after registration
        login(request, user)
        return redirect('login')  # Redirect to a success page or any other desired URL
    
    
    return render(request, 'registration.html')


def home_view(request):
    return render(request,'Index.html')

def finance_view(request):
    return render(request,'finance.html')



