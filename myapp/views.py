from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


def index(request):
   return render(request, 'index.html')
# def category(request):
#    return render(request, 'category.html')
# def contact(request):
#    return render(request, 'contact.html')

