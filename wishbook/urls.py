from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_wish, name="new_wish"),
]

