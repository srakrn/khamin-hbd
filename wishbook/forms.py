from django.forms import ModelForm
from .models import Wish


class WishForm(ModelForm):
    class Meta:
        model = Wish
        fields = ["wish_text", "wish_owner"]
