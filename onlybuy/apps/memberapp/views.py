from django.shortcuts import render

# Create your views here.
def product_details(request):
    return render(request, "index.html")

