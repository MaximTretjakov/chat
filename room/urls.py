from django.urls import path
from django.contrib.auth.decorators import login_required

from room.views import Room


urlpatterns = [
    path('', login_required(Room.as_view()), name='room')
]
