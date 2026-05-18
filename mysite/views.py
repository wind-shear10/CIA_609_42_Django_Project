from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    header = "About us"
    staff = ['John Nichols', "John Rogers", 'Timothy Smith']
    director = {"name": "David Lee", "img": '/director.jpg'}
    address = ['20 V/ 34th St.', 'New York', "NY 10001", 'USA']
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)

def homepage(request):
    data = {"header": "Homepage", "message": "Welcome to My Site!"}
    return render (request, "homepage.html", data)