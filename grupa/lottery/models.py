from django.contrib.auth.models import User
from django.db import models


class LotteryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=200)
    user_mail = models.EmailField(max_length=200)
    has_been_diced = models.BooleanField(default=False)
    who_hit = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name



# user is logging in -> index -> get user_name(pk=user)
# user is dicing -> list all users has_been_diced=0-> if not user -> who_hit -> target
# target -> has_been_diced = 1
# user sees who_hit on page
#
#
#