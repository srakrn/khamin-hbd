from django.forms import ModelForm
from .models import Wish
from captcha.fields import ReCaptchaField


class WishForm(ModelForm):
    captcha = ReCaptchaField(label="กรุณายืนยันว่าคุณไม่ใช่บอท")

    class Meta:
        model = Wish
        fields = ["wish_text", "wish_owner"]
