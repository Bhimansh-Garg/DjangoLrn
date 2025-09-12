from django.http import HttpResponse
from django.shortcuts import render

def Home(Request):
    # return HttpResponse("Lets Start DjangoLrn")
    return render(Request,'websites/index.html')
def about(Request):
    return render(Request,'Websites/about.html')
def contact(Request):
    return render(Request,'websites/contact.html')
