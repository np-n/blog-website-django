from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# To add check point if user who are not logged in try to get profile
# We will do it using decorators
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    # If form submit method is POST then store post content in form variable
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        # If all form input are valid, then send success message
        if form.is_valid():
            # To save all form input to database
            form.save()
            # To get username and return message status to user
            username = form.cleaned_data.get('username')
            # messages.success(request,f'Account created for {username}!')
            # # if submitted info are valid then we redirect users to home page
            # return redirect('blog-home')
            messages.success(request,f'Hi! {username}, your account has been created! Now you are able to log in')
            return redirect('login')


    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')
