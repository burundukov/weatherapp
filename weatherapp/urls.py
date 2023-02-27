from django.contrib import admin
from django.urls import path

from django.conf.urls import url

from weather.views import index_page, find_weather_in_city

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name = 'home'),
    path('weather/', find_weather_in_city, name = 'weather'),
]
