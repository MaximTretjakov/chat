from django.views.generic.base import View
from django.shortcuts import render


class Room(View):

    def get(self, request):
        return render(request, 'room.html')
