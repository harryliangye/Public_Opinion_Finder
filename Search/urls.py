from django.conf.urls import url
from . import views
app_name = 'Search'
urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
	url(r'^find/$', views.find, name='find'),
	url(r'^find/SentimentView/$', views.SentimentView, name='SentimentView'),
]