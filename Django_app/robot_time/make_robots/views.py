from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from make_robots.models import Robot
from .forms import RobotForm


def all_robots(request):
    bots = Robot.objects.all().order_by('name')
    welcome = 'Hey {user}! Let\'s make some robots.'.format(user=request.user)
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


def edit_bot(request):
    # import pdb; pdb.set_trace()
    robot = Robot.objects.get(name=request.POST['robot_name'])
    if request.POST['submitButton'] == 'Update':
        robot.strength = request.POST['robot_strength']
        robot.agility = request.POST['robot_agility']
        robot.armour = request.POST['robot_armour']
        robot.save()
    elif request.POST['submitButton'] == 'Delete':
        robot.delete()

    return redirect('all_robots')


