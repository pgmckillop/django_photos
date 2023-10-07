from django.shortcuts import render

# Home page view
def index(request):
    return render(request, "pages/index.html", {})


# About view
def about(request):
    return render(request, "pages/about.html", {})

# Contact view
def contact(request):
    return render(request, "pages/contact.html", {})
