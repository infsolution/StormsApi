from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'pk', 'username' )

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Comentario
		fields = ('url','pk', 'conteudo', 'date_time', 'atributo','owner')

class AtributoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	comentarios = ComentarioSerializer(many=True, read_only=True)
	responsavel = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	class Meta:
		model = Atributo
		fields = ('url','pk','descricao','responsavel','andamento', 'scopo', 'comentarios','owner')
class ScopoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	atributos = AtributoSerializer(many=True, read_only=True)
	class Meta:
		model = Scopo
		fields = ('url','pk', 'projeto', 'descricao','andamento', 'atributos','owner')

class RespostaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	#mensagem = serializers.SlugRelatedField(queryset=Mensagem.objects.all(), slug_field='conteudo')
	class Meta:
		model = Resposta
		fields = ('url','pk','conteudo','date_time','mensagem', 'owner')
class MensagemSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	respostas = RespostaSerializer(many=True, read_only=True)
	class Meta:
		model = Mensagem
		fields = ('url', 'pk', 'conteudo','date_time', 'chat', 'respostas','owner')

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	colaboradores = UserSerializer(many=True, read_only=True)
	mensagens = MensagemSerializer(many=True, read_only=True)
	scopo = ScopoSerializer(read_only=True)
	interessado = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=False)
	class Meta:
		model = Projeto
		fields = ('url', 'pk', 'nome', 'data_inicio', 'previsao_entrega', 'data_contrato','colaboradores',
									'scopo', 'date_time', 'interessado', 'mensagens', 'owner')

class ProjetoAddColaboradorSerializer(serializers.HyperlinkedModelSerializer):
	colaboradores = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all())
	class Meta:
		model = Projeto
		fields = ('url','pk','colaboradores')

class ForumRespostaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = ForumResposta
		fields = ('url', 'pk', 'conteudo', 'date_time','owner', 'pergunta')

class ForumPerguntaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	respostas = ForumRespostaSerializer(many=True, read_only=True)
	class Meta:
		model = ForumPergunta
		fields = ('url','pk','titulo','descricao', 'date_time', 'aberto', 'respostas', 'owner')