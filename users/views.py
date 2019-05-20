from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.template import RequestContext


# Create your views here.

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user or None, request.POST or None)
        if form.is_valid():
            form.save() 
            update_session_auth_hash(request,form.user)  
            return redirect('/index/')
        else:
            return render(request,'users/change_password.html', {'form':form})
        
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'users/change_password.html',{'form':form})
   
   