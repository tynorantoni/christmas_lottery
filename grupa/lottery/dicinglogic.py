import random

from lottery.models import LotteryModel


class DicingLogic:

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
