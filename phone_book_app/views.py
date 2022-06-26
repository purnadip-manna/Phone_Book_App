from django.shortcuts import redirect, render
from django.utils.html import escape

from phone_book_app.queries import *

# Create your views here.
def show_form(request):
    return render(request, 'form.html')

def add_contact(request):
    fname = escape(request.GET.get('fname'))
    lname = escape(request.GET.get('lname'))
    phnno = escape(request.GET.get('phnno'))
    insert(fname, lname, phnno)
    return redirect("index_page")

def delete_contact(request, id):
    delete(id)
    return redirect("index_page")