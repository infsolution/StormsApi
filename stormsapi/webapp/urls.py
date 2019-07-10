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
	path('forum/', views.forum, name='forum'),
	path('newforum/', views.add_forum, name='newforum'),
	path('respostaforum/<int:id>/', views.add_resposta_forum, name='resposta_forum'),
	path('forum/<int:id>/', views.detail_forum, name='forum_detail'),
	path('editforum/<int:id>/', views.edit_forum, name='forum_edit'),
	path('closeforum/<int:id>/', views.close_forum, name='forum_close'),
	path('openforum/<int:id>/', views.open_forum, name='forum_open'),
	path('deleteforum/<int:id>/', views.delete_forum, name='forum_delete'),
	path('editresposta/<int:id>/', views.edit_resposta, name='resposta_edit'),
	path('deleteresposta/<int:id>/', views.delete_resposta, name='resposta_delete'),
	path('atributos/', views.atributos, name='atributos'),
	path('comentario/', views.comentario_add, name='comentario_add'),
	path('scopo/', views.scopo, name='scopo'),
	path('scopo/<int:id>/', views.scopo_detail, name='scopo_detail'),
	path('addatributo', views.atributo_add, name='atributo_add'),
]