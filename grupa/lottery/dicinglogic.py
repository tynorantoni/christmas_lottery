import random


class DicingLogic:

    def lets_roll(self):
        logged_user = 'pawel'
        counter = 0
        mail_list = ['pawel', 'kasia', 'magda', 'joanna', 'dorota']

        while mail_list:
            counter += 1
            your_person = random.choice(mail_list)
            if not your_person == logged_user:
                mail_list.remove(your_person)
                print("I've turned {} times".format(counter))
                print(mail_list)
                return your_person
