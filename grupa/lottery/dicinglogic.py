import random

from lottery.models import LotteryModel


class DicingLogic:

    def lets_roll(self):
        santas_list = LotteryModel.objects.values_list('user_name').filter('has_been_diced' == False)

        logged_user = 'pawel'
        counter = 0

        while santas_list:
            counter += 1
            your_dice = random.choice(santas_list)
            if your_dice is not logged_user:
                db_model = LotteryModel.objects.get(user_name=your_dice)
                db_model.has_been_diced = True
                db_model.save()
                print("I've turned {} times".format(counter))
                print(santas_list)
                return your_dice
