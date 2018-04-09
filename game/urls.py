from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^',views.mystery,name='game_mystery' ),
    ]