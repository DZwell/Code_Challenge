from django import forms

from .models import Robot


class RobotForm(forms.ModelForm):
    class Meta:
        strength = forms.IntegerField()
        model = Robot
        fields = ['name', 'strength', 'agility', 'armour']
