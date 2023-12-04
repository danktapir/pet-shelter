from django.shortcuts import render
from .forms import EditProfileForm

# Create your views here.
def index(request):
    return render(request, 'my_profile.html')

def edit_profile(request):
    form = EditProfileForm(request.POST)
    if (form.is_valid()):
        cleaned_form = form.cleaned_data
        

    return render(request, 'form_edit_profile.html')