from django.urls import path
#from Home.views import Main
from . import views
main = views.Main()

urlpatterns = [
    #url for open index.html and grap data from remote & Robot
    path('',main.main),
    #url for ajax to reload new values of data 
    path('getd/',main.recievedata,),

]