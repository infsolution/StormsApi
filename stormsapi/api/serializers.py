from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'pk', 'username', 'email', 'password')

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Comentario
		fields = ('url','pk', 'conteudo', 'date_time', 'atributo','owner')
class MembroSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Membro
		fields = ('url','pk','nome','user', 'matricula', 'cpf','owner')

class InteressadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Interessado
		fields = ('url','pk','nome','user', 'cpf')

class AtributoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	comentario= serializers.StringRelatedField(many=True)
	class Meta:
		model = Atributo
		fields = ('url','pk','descricao','responsavel','andamento', 'scopo', 'comentarios','owner')
class ScopoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	atributos = serializers.StringRelatedField(many=True)
	class Meta:
		model = Scopo
		fields = ('url','pk','descricao','andamento', 'atributos','owner')

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	gerente = serializers.SlugRelatedField(queryset=Membro.objects.all(), slug_field='nome')
	membros = serializers.StringRelatedField(many=True)
	class Meta:
		model = Projeto
		fields = ('url', 'pk', 'nome', 'gerente', 'data_inicio', 'previsao_entrega', 'data_contrato','membros',
			'scopo','date_time', 'interessado','owner')
class MensagemSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	respostas = serializers.StringRelatedField(many=True)
	class Meta:
		model = Mensagem
		fields = ('url', 'pk', 'membro','conteudo','date_time', 'respostas','owner')
class RespostaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Resposta
		fields = ('url','pk','conteudo','date_time','mensagem','membro','owner')
class ChatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Chat
		fields = ('url','pk', 'inicio_chat', 'mensagens')

class ForumPerguntaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	membro = serializers.SlugRelatedField(queryset=Membro.objects.all(), slug_field='nome')
	class Meta:
		model = ForumPergunta
		fields = ('url','pk','titulo','descricao', 'membro', 'date_time', 'aberto','owner')

class ForumRespostaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = ForumResposta
		fields = ('url', 'pk', 'conteudo', 'pergunta', 'membro', 'date_time','owner')