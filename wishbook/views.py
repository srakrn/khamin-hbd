from django.shortcuts import render
from django.http import HttpResponse
from .models import Wish

# Create your views here.


def index(request):
    all_wishes = Wish.objects.filter(shown__exact=True).order_by("-created")
    return render(request, "pages/index.html", {"all_wishes": all_wishes})
