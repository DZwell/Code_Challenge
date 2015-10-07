from django.shortcuts import render
from django.http import HttpResponseRedirect

from make_robots.models import Robot
from .forms import RobotForm


def all_robots(request):
    bots = Robot.objects.all().order_by('name')
    welcome = 'Hey %s! Let\'s make some robots.' % (request.user)
    form = RobotForm(request.POST or None)

    if (form.is_valid()):
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('')
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


def edit_bot(request):
    # import pdb; pdb.set_trace()
    robot_strength = Robot.objects.get(strength=request.POST['robot_strength'])
    robot_strength.save()
    robot_agility = Robot.objects.get(agility=request.POST['robot_agility'])
    robot_agility.save()
    robot_armour = Robot.objects.get(armour=request.POST['robot_armour'])
    robot_armour.save()

    context = {
        'robot_strength': robot_strength,
        'robot_agility': robot_agility,
        'robot_armour': robot_armour
    }

    return render(request, 'make_robots/allrobots.html', context)


