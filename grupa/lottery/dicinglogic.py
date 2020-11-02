import random

from lottery.models import LotteryModel


class DicingLogic:


    def check_if_diced(self, logged_user):
        santas_list = LotteryModel.objects.all().filter(who_hit=logged_user).values_list('user_name', flat=True)
        print(santas_list,santas_list.count())
        if santas_list.count() >0:
            return santas_list[0]
        else:
            return False

    def lets_roll(self, logged_user):
        santas_list = LotteryModel.objects.all().filter(has_been_diced=False)

        while santas_list:
            your_dice = random.choice(santas_list)
            if str(your_dice) != str(logged_user):
                db_model = LotteryModel.objects.get(user_name=your_dice)
                db_model.has_been_diced = True
                db_model.who_hit = str(logged_user)
                db_model.save()
                return your_dice
            elif str(your_dice) == str(logged_user) and santas_list.count() != 1:
                continue
            else:
                break
