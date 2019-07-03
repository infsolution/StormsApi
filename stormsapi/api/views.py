from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from .serializers import *
from .permissions import *
from .models import *
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'
	def perform_create(self, serializer):
		instance = serializer.save()
		instance.set_password(instance.password)
		instance.save()
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'user-detail'
class ComentarioList(generics.ListCreateAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer
	name = 'comentario-list'
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'comentario-detail'
class MembroList(generics.ListCreateAPIView):
	queryset = Membro.objects.all()
	serializer_class = MembroSerializer
	#permission_classes = (permissions.IsAuthenticated),
	name = 'membro-list'
class MembroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Membro.objects.all()
	serializer_class = MembroSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'membro-detail'
class InteressadoList(generics.ListCreateAPIView):
	queryset = Interessado.objects.all()
	serializer_class = InteressadoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'interessado-list'
class InteressadoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Interessado.objects.all()
	serializer_class = InteressadoSerializer
	name = 'interessado-detail'
class AtributoList(generics.ListCreateAPIView):
	queryset = Atributo.objects.all()
	serializer_class = AtributoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'atributo-list'
class AtributoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Atributo.objects.all()
	serializer_class = AtributoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'atributo-detail'
class ScopoList(generics.ListCreateAPIView):
	queryset = Scopo.objects.all()
	serializer_class = ScopoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'scopo-list'
class ScopoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Scopo.objects.all()
	serializer_class = ScopoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'scopo-detail'
class ProjetoList(generics.ListCreateAPIView):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'projeto-list'
class ProjetoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'projeto-detail'
class MensagemList(generics.ListCreateAPIView):
	queryset = Mensagem.objects.all()
	serializer_class = MensagemSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'mensagem-list'
class MensagemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Mensagem.objects.all()
	serializer_class = MensagemSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'mensagem-detail'
class RespostaList(generics.ListCreateAPIView):
	queryset = Resposta.objects.all()
	serializer_class = RespostaSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'resposta-list'
class RespostaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Mensagem.objects.all()
	serializer_class = RespostaSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'resposta-detail'
class ChatList(generics.ListCreateAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'chat-list'
class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'chat-detail'

class ForumPerguntaList(generics.ListCreateAPIView):
	queryset = ForumPergunta.objects.all()
	serializer_class = ForumPerguntaSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'forumpergunta-list'
class ForumPerguntaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ForumPergunta.objects.all()
	serializer_class = ForumPerguntaSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'forumpergunta-detail'

class ForumRespostaList(generics.ListCreateAPIView):
	queryset = ForumResposta.objects.all()
	serializer_class = ForumRespostaSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'forum_resposta-list'
class ForumRespostaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ForumResposta.objects.all()
	serializer_class = ForumRespostaSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'forum_resposta-detail'
