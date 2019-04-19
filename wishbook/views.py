from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wish
from .forms import WishForm
from django.contrib import messages


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
        if form.is_valid():
            wish = form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                """ส่งคำอวยพรให้ขมิ้นสำเร็จแล้ว! ทวิตอวยพรด้วยข้อความเมื่อกี้ได้ด้วยการกดปุ่มนี้ 
                    <a class="twitter-share-button"
                    href='https://twitter.com/intent/tweet?url=hbdcherprang.herokupp.com&text={}%20#Born2BeKhamin'>Tweet</a></p>""".format(
                    wish.wish_text
                ),
            )
            return redirect("index")
        else:
            return render(request, "pages/new_wish.html", {"form": form})
