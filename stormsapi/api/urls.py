from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('comentario/', views.ComentarioList.as_view(), name=views.ComentarioList.name),
    path('comentario/<int:pk>/', views.ComentarioDetail.as_view(), name=views.ComentarioDetail.name),
    path('membro/', views.MembroList.as_view(), name=views.MembroList.name),
    path('membro/<int:pk>/', views.MembroDetail.as_view(), name=views.MembroDetail.name),
    path('interessado/', views.InteressadoList.as_view(), name=views.InteressadoList.name),
    path('interessado/<int:pk>/', views.InteressadoDetail.as_view(), name=views.InteressadoDetail.name),
    path('atributo/', views.AtributoList.as_view(), name=views.AtributoList.name),
    path('atributo/<int:pk>/', views.AtributoDetail.as_view(), name=views.AtributoDetail.name),
    path('scopo/', views.ScopoList.as_view(), name=views.ScopoList.name),
    path('scopo/<int:pk>/', views.ScopoDetail.as_view(), name=views.ScopoDetail.name),
    path('projeto/', views.ProjetoList.as_view(), name=views.ProjetoList.name),
    path('projeto/<int:pk>/', views.ProjetoDetail.as_view(), name=views.ProjetoDetail.name),
    path('mensagem/', views.MensagemList.as_view(), name=views.MensagemList.name),
    path('mensagem/<int:pk>/', views.MensagemDetail.as_view(), name=views.MensagemDetail.name),
    path('resposta/', views.RespostaList.as_view(), name=views.RespostaList.name),
    path('resposta/<int:pk>/', views.RespostaDetail.as_view(), name=views.RespostaDetail.name),
    path('chat/', views.ChatList.as_view(), name=views.ChatList.name),
    path('chat/<int:pk>/', views.ChatDetail.as_view(), name=views.ChatDetail.name),
    path('forum-pergunta/', views.ForumPerguntaList.as_view(), name=views.ForumPerguntaList.name),
    path('forum-pergunta/<int:pk>/', views.ForumPerguntaDetail.as_view(), name=views.ForumPerguntaDetail.name),
    path('forum-resposta/', views.ForumRespostaList.as_view(), name=views.ForumRespostaList.name),
    path('forum-resposta/<int:pk>/', views.ForumRespostaDetail.as_view(), name=views.ForumRespostaDetail.name),
]
