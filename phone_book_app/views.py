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

def edit_contact(request, id):
    obj = get_by_id(id)
    data = {
        "update" : True,
        "id" : obj.id,
        "fname" : obj.fname,
        "lname" : obj.lname,
        "phnno" : obj.phnno
    }
    return render(request, 'form.html', data)

def update_contact(request):
    id = int(escape(request.GET.get('id')))
    fname = escape(request.GET.get('fname'))
    lname = escape(request.GET.get('lname'))
    phnno = escape(request.GET.get('phnno'))
    update(id, fname, lname, phnno)
    return redirect("index_page")