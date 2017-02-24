from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^callback/getfac', views.get_faculties, name='get_facs'),
    url(r'^callback/getdeps', views.get_departments, name='get_deps'),
    url(r'^getresults/inputs', views.get_input, name='get_input'),
    url(r'^getresults/results', views.get_results, name='get_resutls'),
    url(r'^getresults/seeding_subjects', views.seeding_subjects, name='seeding_subjects'),
    url(r'^getresults/seeding', views.seeding_table, name='seeding_table'),

]