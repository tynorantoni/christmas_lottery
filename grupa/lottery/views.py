from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required
from lottery.dicinglogic import DicingLogic


def index(request):
    hey_santa = 'lov ya' #DicingLogic().lets_roll()
    context={}
    # response.user.todolist.add(t)  # adds the to do list to the current logged in user
    if (request.POST.get('trig_dice')):
        print('working!')
        is_true = True
        context={'hey_santa':hey_santa,
                 'is_true':is_true}
    if request.POST.get('trig_play'):
        print('siemka')
    return render(request,'lottery/index.html',context)


def register(request):
    pass