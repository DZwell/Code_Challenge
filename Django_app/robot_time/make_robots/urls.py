from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_robots, name='all_robots')
]
