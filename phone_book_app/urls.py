from django.urls import path
from phone_book_app.views import *

urlpatterns = [
    path('', show_form),
    path('add/', add_contact),
    path('delete/<int:id>', delete_contact),
    path('edit/<int:id>', edit_contact),
    path('update/', update_contact),
]
