from django.conf.urls import url 
from . import views

app_name = 'polls' #so that we can specifiy app name when calling {% url %} in template
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
]