from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='blog'),
    url(r'^(?P<pk>\d+)$', views.DetailView.as_view(), name='post'),
        ]
