from django.urls import path
from .views import *
urlpatterns = [
    path("",booklist),
    path("add/",post_Book),
    path("update/<int:id>/",update_Book),
    path("delete/<int:id>/",delete_Book) 
]
