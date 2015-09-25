    # import pdb; pdb.set_trace()
from django.shortcuts import render

from make_robots.models import Robot
from .forms import RobotForm


def all_robots(request):
    bots = Robot.objects.all().order_by('name')
    welcome = 'Hey %s! Let\'s make some robots.' % (request.user)
    form = RobotForm(request.POST or None)

    if (form.is_valid()):
        instance = form.save()
        instance.save()
    context = {
        'robots': bots,
        'welcome': welcome,
        'form': form,
    }
    return render(request, 'make_robots/allrobots.html', context)


def delete_bot(request):
    this_bot = Robot.objects.filter(name=request.POST['robot_name'])
    this_bot.delete()

    context = {
        'this_bot': this_bot
    }

    return render(request, 'make_robots/allrobots.html', context)


