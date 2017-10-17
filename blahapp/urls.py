from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', views.cat_list, name='cat_list'),
	url(r'^cat/new/$', views.cat_new, name='cat_new'),
	url(r'^cat/(?P<pk>\d+)/$', views.cat_detail, name='cat_detail'),
	url(r'^cat/(?P<pk>\d+)/edit/$', views.cat_edit, name='cat_edit'),
	url(r'^cat/(?P<pk>\d+)/delete/$', views.cat_delete, name='cat_delete'),

	url(r'^accounts/login/', auth_views.login, name='login'),
	url(r'^accounts/logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^accounts/profile/', views.cat_list, name='profile'), # Cheat and just redirect to home	
]
