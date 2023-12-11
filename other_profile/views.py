from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import ReportForm
from .models import Report

User = get_user_model()

# Create your views here.
def profile(request, username):
    user = request.user
    reported_user = get_object_or_404(User, username=username)
    context = {'user': user, 'reported_user': reported_user}
    return render(request, 'profile.html', context)

def report_user(request, username):
    reported_user = get_object_or_404(User, username=username)
    user = request.user
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            Report.objects.create(
                reported_user=reported_user,
                reason=reason,
            )
            context = {'user': user, 'reported_user': reported_user}
            return render(request, 'profile.html', context)
    else:
        form = ReportForm()
        
    context = {'form': form, 'reported_user': reported_user}
    return render(request, 'report.html', context)
