from django.urls import path
from . import views

app_name = 'csvapp'

urlpatterns = [

     path('',views.uploadfile,name='uploadfile'),
     path('result/',views.result,name='result'),

]