from django.db import models


class LotteryModel(models.Model):
    user_name = models.CharField(max_length=200)
    user_mail = models.EmailField(max_length=200)
    has_been_diced = models.BooleanField(default=False)
    who_hit = models.CharField(max_length=200)