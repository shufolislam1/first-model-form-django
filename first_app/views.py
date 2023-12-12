from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = forms.studentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = forms.studentForm()
    return render(request,'home.html', {'data': form})