from django.contrib import admin

from .forms import RobotForm
from .models import Robot


class RobotAdmin(admin.ModelAdmin):
    list_display = ['name', 'updated']
    form = RobotForm

admin.site.register(Robot, RobotAdmin)
