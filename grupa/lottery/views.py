from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# @login_required
from lottery.dicinglogic import DicingLogic
from lottery.models import LotteryModel


def index(request):
    hey_santa = 'lov ya'  # DicingLogic().lets_roll()

    user_object = LotteryModel.objects.filter(user=User.objects.get(username=request.user))
    context = {'user_obj': user_object}

    if (request.POST.get('trig_dice')):
        print('working!')
        is_true = True
        context = {'hey_santa': hey_santa,
                   'is_true': is_true}
    if request.POST.get('trig_play'):
        print('siemka')
    return render(request, 'lottery/index.html', context)


def register(request):
    pass
