from django.shortcuts import render

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def all_finches(request):
    return render(request, 'all-finches.html')