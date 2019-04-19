from django.db import models

# Create your models here.


class Wish(models.Model):
    wish_text = models.TextField(verbose_name="ข้อความอวยพร")
    wish_owner = models.CharField(verbose_name="ชื่อผู้อวยพร", max_length=50)
    shown = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} from {}".format(
            self.wish_text[: min(len(self.wish_text), 10)], self.wish_owner
        )
