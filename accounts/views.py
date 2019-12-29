from django.views.generic.base import View
from django.shortcuts import render, redirect


class SwitchTo(View):

    def get(self, request, *args, **kwargs):
        return redirect('/accounts/login/')
