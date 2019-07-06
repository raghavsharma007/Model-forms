from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import FormFill

def home(request):
    if request.method == 'POST':
        form = FormFill(request.POST)
        if form.is_valid():
            detail=form.save(commit=False)
            detail.save()
            return redirect('register:home')



    form = FormFill()
    return render(request, 'register/formpage.html',{'form':form})