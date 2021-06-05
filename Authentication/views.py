from .auth import UserRegistrationForm
from django.shortcuts import render , redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request,f'Account Created {name}')
            return redirect('../../blog')

    else:
        form = UserRegistrationForm()
    return render(request,'Authentication/register.html',{'form':form})

  

