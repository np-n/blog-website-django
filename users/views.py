from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
            messages.success(request,f'Hi {username}, your account has been created! Now you are able to log in')
            return redirect('login')


    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    # If form submit method is POST then store post content in form variable
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        # If all form input are valid, then send success message
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Hi {request.user.username}, your account has been updated!')
            return redirect('profile')



    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    # To pass both update form we will a dictionary
    context = {
        'u_form': u_form,
        'p_form': p_form
        }
    return render(request,'users/profile.html',context)
