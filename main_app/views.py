from django.shortcuts import render

# Create your views here.

# define home view here - '/'
# GET - Home
def home(request):
    # unlike with ejs, we need our .html file extension
    return render(request, 'home.html')