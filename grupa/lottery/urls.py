from django.urls import path
from . import views



app_name='lottery'

urlpatterns= [
    path('',views.index, name='index'),

]
