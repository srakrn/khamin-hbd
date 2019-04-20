from django.forms import ModelForm, Textarea
from .models import Wish
from captcha.fields import ReCaptchaField


class WishForm(ModelForm):
    captcha = ReCaptchaField(
        label="กรุณายืนยันว่าคุณไม่ใช่บอท",
        error_messages={"required": "กรุณายืนยันว่าไม่ใช่บอท"},
    )

    class Meta:
        model = Wish
        fields = ["wish_text", "wish_owner"]
        widgets = {"wish_text": Textarea(attrs={"rows": 3})}
        error_messages = {
            "wish_text": {"required": "กรุณาระบุข้อความอวยพร"},
            "wish_owner": {"required": "กรุณาระบุชื่อ"},
        }

