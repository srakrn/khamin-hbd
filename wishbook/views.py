from django.shortcuts import render
from django.http import HttpResponse
from .models import Wish
from .forms import WishForm

# Create your views here.


def index(request):
    all_wishes = Wish.objects.filter(shown__exact=True).order_by("-created")
    return render(request, "pages/index.html", {"all_wishes": all_wishes})


def new_wish(request):
    if request.method == "GET":
        form = WishForm()
        return render(request, "pages/new_wish.html", {"form": form})
    else:
        form = WishForm(request.POST)
        form.save()
        return HttpResponse("เรียบร้อยส์")
