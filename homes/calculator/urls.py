from django.conf.urls import url

from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calculate/', views.calculate, name='calculate'),
    url(r'^results/', views.results, name='results'),
]
