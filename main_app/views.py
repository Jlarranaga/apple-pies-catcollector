from django.shortcuts import render

# Add this cats list below the imports
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Donut', 'breed': 'siamese', 'description': 'cute but kinda scary', 'age': 0},
]

# Create your views here.

# define home view here - '/'
# GET - Home
def home(request):
    # unlike with ejs, we need our .html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# index view - shows all the cats at '/cats'
def cats_index(request):
    # just like in ejs, we can pass some data to our views
    return render(request, 'cats/index.html', { 'cats': cats })