from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('GetPrice', views.request_server, name='request_server'),
    path('UpdatePrice', views.update_price, name='update_price'),
]

urlpatterns += staticfiles_urlpatterns()