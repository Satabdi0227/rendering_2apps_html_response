from django.urls import path
from app1.views import *

app_name = 'something'

urlpatterns = [
    path('first_page/',first_page,name='first_page'),
    path('second_page/',second_page,name='second_page'),
]