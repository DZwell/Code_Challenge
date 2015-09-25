from django.shortcuts import render
from make_robots.models import Robot
from .forms import RobotForm

    # import pdb; pdb.set_trace()

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


    # For Delete button:
    def delete_bot(request):
        this_bot = Robot.name.delete(request.POST)

        context = {
            'this_bot': this_bot
        }

        return render(request, 'make_robots/allrobots.html', context)
    # Write delete view
    # Go into URLS create route
    # Grab individual instance of Robot
        # using .name


def new_robot(request):
    form = RobotForm(request.POST or None)

    if (form.is_valid()):
        instance = form.save()
        instance.save()

    context = {
        'form': form
    }
    return render(request, 'make_robots/allrobots.html', context)

