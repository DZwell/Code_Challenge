from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_robots, name='all_robots'),
    url(r'^deletebot/$', views.delete_bot, name='delete_bot'),
    # url(r'^CallWhatever/&', views.DELETEMethod, name='HTML referrences this name in Form action attribute)

]
