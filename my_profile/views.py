from django.shortcuts import redirect, render
from .forms import EditProfileForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def index(request):
    return render(request, "my_profile.html")


def edit_profile(request):
    form = EditProfileForm(request.POST or None)
    if form.is_valid():
        cleaned_form = form.cleaned_data
        username = cleaned_form.get("username")
        email = cleaned_form.get("email")
        password = cleaned_form.get("password")
        address = cleaned_form.get("address")
        phone_num = cleaned_form.get("phone")

        user = User.objects.get(username=request.user.username)

        if len(username) != 0:
            user.username = username
        if len(email) != 0:
            user.email = email
        if len(password) != 0:
            user.password = password
        if len(address) != 0:
            user.address = address
        if len(phone_num) != 0:
            user.phone_number = phone_num

        return redirect('my-profile/index')

    return render(request, "form_edit_profile.html", context={'form': form})
