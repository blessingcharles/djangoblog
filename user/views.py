from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from Authentication.auth import ProfileUpdateForm , UserUpdateForm
from django.contrib import messages
# Create your views here.

@login_required
def profile(request):

    if request.method == 'POST':

        userUpdateForm = UserUpdateForm(request.POST,
                                        instance=request.user)

        profileUpdateForm = ProfileUpdateForm(request.POST,
                                            request.FILES,
                                            instance=request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request,'Your Account is Updated')
            
    else: 
        userUpdateForm = UserUpdateForm(instance=request.user)
        profileUpdateForm = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'userUpdateForm':userUpdateForm,
        'profileUpdateForm':profileUpdateForm
    }
    
    return render(request,'user/profile.html',context)