from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    std = forms.studentForm
    return render(request,'home.html', {'data': std})