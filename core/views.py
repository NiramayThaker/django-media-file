from django.shortcuts import render

# Create your views here.
def upload_form(request):
    return render(request, 'core/index.html')