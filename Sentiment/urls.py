from django.conf.urls import url
from . import views
app_name = 'Sentiment'
urlpatterns = [
    url(r'^$', views.SentimentTool, name='SentimentTool')
]