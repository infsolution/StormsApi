from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import *
#from api.models import *

@login_required
def index(request):
	projetos = Projeto.objects.filter(owner=request.user.id)
	atributos = Atributo.objects.filter(responsavel=request.user)
	return render(request, 'webapp/home.html', {'perfil_logado': get_user(request), 'projetos':projetos,
		'atributos':atributos})

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'webapp/cadastro.html', context)



def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect('index')
	return render(request, 'webapp/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')
@login_required
def userPage(request):
	projetos = Projeto.objects.filter(owner=request.user.id)
	return render(request, 'webapp/user_page.html', {'perfil_logado': get_user(request), 'projetos': projetos})
@login_required
def get_projeto(request, id):
	projeto = Projeto.objects.get(id=id)
	interessados = Projeto.objects.filter(interessado=request.user)
	membros = User.objects.all()
	return render(request,'webapp/projeto.html', {'perfil_logado': get_user(request),
	 'projeto': projeto, 'membros':membros, 'inter_projetos':interessados})
@login_required
def add_projeto(request):
	if request.method == 'POST':
		inter = User.objects.get(id=request.POST.get('interessado_id'))
		pro = Projeto(owner=request.user, nome=request.POST.get('nome'), data_inicio=request.POST.get('data_inicio'),
		previsao_entrega=request.POST.get('previsao_entrega'), data_contrato=request.POST.get('data_contrato'), interessado=inter)
		pro.save()
		return redirect('/projeto/'+str(pro.id)+'/')
	interessados = User.objects.all()
	return render(request, 'webapp/new_projeto.html',{'perfil_logado': get_user(request), 'interessados':interessados})
@login_required
def get_user(request):
	return request.user
@login_required
def get_atributo(request, id):
	atributo = Atributo.objects.get(id=id)
	return render(request, 'webapp/atributo.html',{'perfil_logado': get_user(request),'atributo':atributo})
@login_required	
def add_membro(request):
	if request.method == 'POST':
		proje = Projeto.objects.get(id=request.POST.get('projeto'))
		mem = User.objects.get(id=request.POST.get('membro'))
		proje.colaboradores.add(mem)
		proje.save()
	return redirect('/projeto/'+str(request.POST.get('projeto'))+'/')
@login_required
def forum(request):
	foruns = ForumPergunta.objects.all()
	return render(request, 'webapp/forum.html',{'perfil_logado': get_user(request),
		'foruns':foruns})
@login_required
def add_forum(request):
	if request.method == 'POST':
		forum = ForumPergunta(owner=request.user, titulo=request.POST.get('titulo'),
			descricao=request.POST.get('descricao'), aberto=1)
		forum.save()
	return redirect('forum')
@login_required
def add_resposta_forum(request, id):
	if request.method == 'POST':
		forum = ForumPergunta.objects.get(id=id);
		resp = ForumResposta(owner=request.user, conteudo=request.POST.get('conteudo'),
			pergunta=forum)
		resp.save()
		print(resp)
	return redirect('forum')
@login_required
def detail_forum(request, id):
	forum = ForumPergunta.objects.get(id=id)
	return render(request, 'webapp/forum-detail.html',{'perfil_logado': get_user(request),
		'forum':forum})
@login_required
def edit_forum(request, id):
	if request.method == 'POST':
		forum = ForumPergunta.objects.get(id=id)
		forum.titulo = request.POST.get('titulo')
		forum.descricao = request.POST.get('descricao')
		forum.save()
	return redirect('/forum/'+str(id)+'/')
@login_required
def close_forum(request, id):
	if request.method == 'GET':
		forum = ForumPergunta.objects.get(id=id)
		forum.aberto = 0
		forum.save()
	return redirect('/forum/'+str(id)+'/')
@login_required
def open_forum(request, id):
	if request.method == 'GET':
		forum = ForumPergunta.objects.get(id=id)
		forum.aberto = 1
		forum.save()
	return redirect('/forum/'+str(id)+'/')	
@login_required	
def delete_forum(request, id):
	if request.method == 'POST':
		forum = ForumPergunta.objects.get(id=id)
		forum.delete()
	return redirect('forum')
@login_required
def delete_resposta(request, id):
	if request.method == 'POST':
		resposta = ForumResposta.objects.get(id=id)
		resposta.delete()
	return redirect('forum')
@login_required	
def edit_resposta(request, id):
	if request.method == 'POST':
		resposta = ForumResposta.objects.get(id=id)
		resposta.conteudo = request.POST.get('conteudo')
		resposta.save()
	return redirect('forum')
@login_required	
def atributos(request):
	atributos = Atributo.objects.filter(responsavel=request.user)
	return render(request, 'webapp/home.html', {'perfil_logado': get_user(request), 'atributos':atributos})
@login_required	
def comentario_add(request):
	if request.method == 'POST':
		atri = Atributo.objects.get(id=request.POST.get('atributo_id'))
		atri.andamento += 5
		atri.save()
		coment = Comentario(owner=request.user,conteudo=request.POST.get('conteudo'), atributo=atri)
		coment.save()
	return redirect('/atributo/'+str(request.POST.get('atributo_id'))+'/')

@login_required	
def scopo(request):
	id_pro = request.POST.get('projeto')
	if request.method == 'POST':
		pro = Projeto.objects.get(id=id_pro)
		scopo = Scopo(owner=request.user, projeto=pro, descricao=request.POST.get('descricao'), andamento=0)
		scopo.save()
	return redirect('/projeto/'+str(id_pro)+'/')
@login_required
def scopo_detail(request, id):
	scopo = Scopo.objects.get(id=id)
	return render(request, 'webapp/scopo_detail.html', {'perfil_logado': get_user(request),'scopo':scopo})

@login_required	
def atributo_add(request):
	if request.method == 'POST':
		scopo = Scopo.objects.get(id=request.POST.get('scopo'))
		responsavel = User.objects.get(id=request.POST.get('responsavel')) 
		atri = Atributo(owner=request.user, descricao=request.POST.get('descricao'),
			responsavel=responsavel, andamento=0, scopo=scopo)
		atri.save()
	return redirect('/scopo/'+str(scopo.id)+'/')
