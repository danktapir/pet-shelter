from django.shortcuts import render

# Create your views here.
def katalog(request):
    return render(request, 'katalog.html')