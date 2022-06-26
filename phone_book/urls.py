from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, "index_page"),
    path('admin/', admin.site.urls),
    path('app/', include('phone_book_app.urls'))
]
