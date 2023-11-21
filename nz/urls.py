from nz.views import *
from django.urls import path
app_name='kane'
urlpatterns=[
    path('kane/',kane,name='kane'),
    ]