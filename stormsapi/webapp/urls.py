from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('cadastro/', views.cadastro, name='cadastro'),
 	path('login/',views.do_login, name='login'),
	path('logout/',views.do_logout, name='logout'),
	path('user/', views.userPage, name='user'),
	path('add/', views.add_projeto, name='add'),
	path('addmembro/', views.add_membro, name='addmembro'),
	path('projeto/<int:id>/', views.get_projeto, name='projeto'),
	path('atributo/<int:id>/', views.get_atributo, name='atributo'),
	path('forum', views.forum, name='forum'),
	path('newforum', views.add_forum, name='newforum'),
]