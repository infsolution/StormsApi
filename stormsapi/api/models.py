from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models

class Projeto(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerprojeto', on_delete=models.CASCADE)
	nome = models.CharField(max_length=200)
	data_inicio = models.DateField()
	previsao_entrega = models.DateField()
	data_contrato = models.DateField()
	colaboradores = models.ManyToManyField(User)
	date_time = models.DateTimeField(auto_now_add=True)
	interessado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interessado', null=True)
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.nome

class Scopo(models.Model):#Erro
	owner = models.ForeignKey('auth.User', related_name='ownerscopo', on_delete=models.CASCADE)
	projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE, related_name='scopo', null=True)
	descricao = models.CharField(max_length=256)
	andamento = models.IntegerField(default=0)
	def __str__(self):
		return self.descricao
class Atributo(models.Model):
	owner = models.ForeignKey('auth.User', related_name='owneratributo', on_delete=models.CASCADE)
	descricao = models.CharField(max_length=256)
	responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsavel', null=True)
	andamento = models.IntegerField(default=0)
	scopo = models.ForeignKey(Scopo, on_delete=models.CASCADE, related_name='atributos')
	def __str__(self):
		return self.descricao

class Comentario(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownercomentario', on_delete=models.CASCADE)
	conteudo = models.CharField(max_length=256)
	date_time = models.DateTimeField(auto_now_add=True)
	atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE, related_name='comentarios')
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.conteudo



class Mensagem(models.Model):#Deu Erro
	owner = models.ForeignKey('auth.User', related_name='ownermensage', on_delete=models.CASCADE)
	conteudo = models.CharField(max_length=256)
	date_time = models.DateTimeField(auto_now_add=True)
	chat = models.ForeignKey(Projeto, related_name='mensagens',on_delete=models.CASCADE)
	class Meta:
		ordering =('-date_time',)
	def __str__(self):
		return self.conteudo
class Resposta(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerresposta', on_delete=models.CASCADE)
	conteudo = models.CharField(max_length=256)
	date_time = models.DateTimeField(auto_now_add=True)
	mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE, related_name='respostas')
	def __str__(self):
		return self.conteudo



class ForumPergunta(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerforuns', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=256)
	descricao = models.CharField(max_length=512, null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	aberto = models.BooleanField(default=True)
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.titulo

class ForumResposta(models.Model):#Erro
	owner = models.ForeignKey('auth.User', related_name='ownerforrespo', on_delete=models.CASCADE)
	conteudo = models.CharField(max_length=256)
	pergunta = models.ForeignKey(ForumPergunta, on_delete=models.CASCADE, related_name='repostas')
	date_time = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.conteudo





