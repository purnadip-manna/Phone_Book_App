from phone_book_app.models import Contact

def insert(fname, lname, phnno):
    obj = Contact(fname=fname, lname=lname, phnno=phnno)
    obj.save()

def fetch():
    return Contact.objects.all()

def delete(id):
    obj = Contact.objects.filter(id=id)
    obj.delete()