from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from make_robots.models import Robot


def all_robots(request):
    bots = Robot.objects.all().order_by('name')
    context = {'robots': bots}
    return render_to_response('allrobots.html', context, context_instance=RequestContext(request))

