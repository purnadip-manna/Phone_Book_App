from django.shortcuts import render

from phone_book_app.queries import fetch

def index(request):
    data = fetch()
    return render(request,'home.html', {'list': data})