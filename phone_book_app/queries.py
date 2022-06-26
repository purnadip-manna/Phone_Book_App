from phone_book_app.models import Contact

def insert(fname, lname, phnno):
    obj = Contact(fname=fname, lname=lname, phnno=phnno)
    obj.save()

def get_by_id(id):
    return Contact.objects.get(id=id)

def fetch():
    return Contact.objects.all()

def delete(id):
    obj = Contact.objects.filter(id=id)
    obj.delete()

def update(id, fname, lname, phnno):
    obj = get_by_id(id)
    obj.fname = fname
    obj.lname = lname
    obj.phnno = phnno
    obj.save()