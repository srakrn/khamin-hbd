from django.shortcuts import render
from django.http import HttpResponse
from .models import Wish

# Create your views here.


def index(request):
    all_wishes = Wish.objects.order_by("-created").all()
    return render(request, "pages/index.html", {"all_wishes": all_wishes})
