from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from lottery.dicinglogic import DicingLogic
from lottery.forms import CustomAuthenticationForm
from lottery.models import LotteryModel


@login_required()
def index(request):
    user = User.objects.get(username=request.user)
    print(user, " user name")

    if (request.POST.get('trig_dice')):
        print('working!')
        hey_santa = DicingLogic().lets_roll(user)
        is_true = True
        context = {'hey_santa': hey_santa,
                   'is_true': is_true,
                   'user_obj': user}
    # if request.POST.get('trig_play'):
    #     print('siemka')
    return render(request, 'lottery/index.html', context)


def view_404(request, exception=None):
    return redirect("/")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
