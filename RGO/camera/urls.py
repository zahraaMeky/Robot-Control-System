from django.urls import path
from . import views


urlpatterns = [

    path('webcam_feed_0/',views.webcam_feed_0,name='webcam_feed_0'),
    path('webcam_feed_1/',views.webcam_feed_1,name='webcam_feed_1'),
    path('webcam_feed_2/',views.webcam_feed_2,name='webcam_feed_2'),
    path('webcam_feed_3/',views.webcam_feed_3,name='webcam_feed_3'),
    path('webcam_feed_4/',views.webcam_feed_4,name='webcam_feed_4'),
    path('webcam_feed_5/',views.webcam_feed_5,name='webcam_feed_5'),

]