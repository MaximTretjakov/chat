from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('room/', include('room.urls')),
    path('', views.SwitchTo.as_view(), name='switch_to')
]
