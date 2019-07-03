from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models


class Membro(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownermembro', on_delete=models.CASCADE)
	nome = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='membro')
	matricula = models.CharField(max_length=10)
	cpf = models.CharField(max_length=15)
	class Meta:
		ordering = ('nome',)
	def __str__(self):
		return self.nome
class Interessado(models.Model):
	nome = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interessado')
	cpf = models.CharField(max_length=15)
	class Meta:
		ordering = ('nome',)
	def __str__(self):
		return self.nome

class Scopo(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerscopo', on_delete=models.CASCADE)
	descricao = models.CharField(max_length=256)
	andamento = models.IntegerField(default=0)
	def __str__(self):
		return self.descricao
class Atributo(models.Model):
	owner = models.ForeignKey('auth.User', related_name='owneratributo', on_delete=models.CASCADE)
	descricao = models.CharField(max_length=256)
	responsavel = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='responsavel', null=True)
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

class Projeto(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerprojeto', on_delete=models.CASCADE)
	nome = models.CharField(max_length=200)
	gerente = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='gerente')
	data_inicio = models.DateField()
	previsao_entrega = models.DateField()
	data_contrato = models.DateField()
	membros = models.ManyToManyField(Membro)
	scopo = models.OneToOneField(Scopo, on_delete=models.CASCADE, related_name='scopo', null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	interessado = models.ForeignKey(Interessado, on_delete=models.CASCADE, related_name='interessado', null=True)
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.nome

class Mensagem(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownermensage', on_delete=models.CASCADE)
	membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='membro')
	conteudo = models.CharField(max_length=256)
	date_time = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering =('-date_time',)
	def __str__(self):
		return self.conteudo
class Resposta(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerresposta', on_delete=models.CASCADE)
	conteudo = models.CharField(max_length=256)
	date_time = models.DateTimeField(auto_now_add=True)
	mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE, related_name='respostas')
	membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='membro_res')
	def __str__(self):
		return self.conteudo
class Chat(models.Model):
	inicio_chat=models.DateTimeField(auto_now_add=True)
	mensagens = models.ManyToManyField(Mensagem)


class ForumPergunta(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerforuns', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=256)
	descricao = models.CharField(max_length=512, null=True)
	membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='pergunta_membro')	
	date_time = models.DateTimeField(auto_now_add=True)
	aberto = models.BooleanField(default=True)
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.titulo

class ForumResposta(models.Model):
	owner = models.ForeignKey('auth.User', related_name='ownerforrespo', on_delete=models.CASCADE)
	conteudo = models.CharField(max_length=256)
	pergunta = models.ForeignKey(ForumPergunta, on_delete=models.CASCADE, related_name='pergunta')
	membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='resposta_membro')
	date_time = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ('-date_time',)
	def __str__(self):
		return self.conteudo





