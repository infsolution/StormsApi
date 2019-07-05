from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions
from django_filters import rest_framework as filters
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from .serializers import *
from .permissions import *
from .models import *

class UserCreate(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer
	def perform_create(self, serializer):
		instance = serializer.save()
		instance.set_password(instance.password)
		instance.save()
	name = 'user-create'

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated),
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	'''def perform_create(self, serializer):
					instance = serializer.save()
					instance.set_password(instance.password)
					instance.save()'''
	name = 'user-list'
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated),
	name = 'user-detail'
class ComentarioList(generics.ListCreateAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'comentario-list'
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'comentario-detail'
class AtributoList(generics.ListCreateAPIView):
	queryset = Atributo.objects.all()
	serializer_class = AtributoSerializer
	permission_classes = (permissions.IsAuthenticated),
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'atributo-list'
class AtributoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Atributo.objects.all()
	serializer_class = AtributoSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'atributo-detail'
class ScopoList(generics.ListCreateAPIView):
	queryset = Scopo.objects.all()
	serializer_class = ScopoSerializer
	permission_classes = (permissions.IsAuthenticated),
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'scopo-list'
class ScopoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Scopo.objects.all()
	serializer_class = ScopoSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'scopo-detail'
class ProjetoList(generics.ListCreateAPIView):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoSerializer
	permission_classes = (permissions.IsAuthenticated),
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'projeto-list'
class ProjetoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoSerializer
	#permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
	name = 'projeto-detail'
class MensagemList(generics.ListCreateAPIView):
	queryset = Mensagem.objects.all()
	serializer_class = MensagemSerializer
	permission_classes = (permissions.IsAuthenticated),
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'mensagem-list'

class MensagemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Mensagem.objects.all()
	serializer_class = MensagemSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'mensagem-detail'
	
class RespostaList(generics.ListCreateAPIView):
	queryset = Resposta.objects.all()
	serializer_class = RespostaSerializer
	permission_classes = (permissions.IsAuthenticated),
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'resposta-list'
class RespostaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Resposta.objects.all()
	serializer_class = RespostaSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'resposta-detail'

class ForumPerguntaList(generics.ListCreateAPIView):
	queryset = ForumPergunta.objects.all()
	serializer_class = ForumPerguntaSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
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
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	name = 'forumresposta-list'
class ForumRespostaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ForumResposta.objects.all()
	serializer_class = ForumRespostaSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'forumresposta-detail'

class ProjetoColaborador(generics.RetrieveUpdateDestroyAPIView):
	queryset = Projeto.objects.all()
	serializer_class = ProjetoAddColaboradorSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
	name = 'projetocolaborador-detail'