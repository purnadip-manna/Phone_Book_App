from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, default="")
    phnno = models.CharField(max_length=12, null=False)

    def __str__(self):
        return self.fname