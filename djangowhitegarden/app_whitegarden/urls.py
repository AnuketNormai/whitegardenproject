from django.urls import path , include
from .views import homePage, mdb_page,waterstorage_page,air_page,floor1_page,floor2_page,floor3_page,floor4_page,floor5_page,room_page,graph_air_page,graph_room_page
from .apiwater import api_water_Data
from .apimdb import api_mdb_Data
from .apiair import api_airfloor1_Data
from .apifloor1 import api_floor1_Data
from .apifloor2 import api_floor2_Data
from .apifloor3 import api_floor3_Data
from .apifloor4 import api_floor4_Data
from .apifloor5 import api_floor5_Data
from .apiroom import api_room_Data
from .apiampkwhtoday import api_ampkwhtoday_Data
from django.urls import path , include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/water', api_water_Data.as_view()),
    path('api/mdb', api_mdb_Data.as_view()),
    path('api/airf1',api_airfloor1_Data.as_view()),
    path('api/floor1', api_floor1_Data.as_view()),
    path('api/floor2', api_floor2_Data.as_view()),
    path('api/floor3', api_floor3_Data.as_view()),
    path('api/floor4', api_floor4_Data.as_view()),
    path('api/floor5', api_floor5_Data.as_view()),
    path('api/room', api_room_Data.as_view()),
    path('api/ampkwhtoday', api_ampkwhtoday_Data.as_view()),
    path('home', homePage),
    path('waterstorage', waterstorage_page),
    path('mdb', mdb_page),
    path('air', air_page),
    path('floor1', floor1_page),
    path('floor2', floor2_page),
    path('floor3', floor3_page),
    path('floor4', floor4_page),
    path('floor5', floor5_page),
    path('room', room_page),
    path('graphair', graph_air_page),
    path('graphroom', graph_room_page),
]