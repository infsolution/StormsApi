from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .forms import *
#from api.models import *

@login_required
def index(request):
	projetos = Projeto.objects.filter(owner=request.user.id)
	return render(request, 'webapp/home.html', {'perfil_logado': get_user(request), 'projetos':projetos})

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

def userPage(request):
	projetos = Projeto.objects.filter(owner=request.user.id)
	return render(request, 'webapp/user_page.html', {'perfil_logado': get_user(request), 'projetos': projetos})
@login_required
def get_projeto(request, id):
	projeto = Projeto.objects.get(id=id)
	membros = User.objects.all()
	return render(request,'webapp/projeto.html', {'perfil_logado': get_user(request),
	 'projeto': projeto, 'membros':membros})
@login_required
def add_projeto(request):
	if request.method == 'POST':
		inter = User.objects.get(id=request.POST.get('interessado_id'))
		pro = Projeto(owner=request.user, nome=request.POST.get('nome'), data_inicio=request.POST.get('data_inicio'),
		previsao_entrega=request.POST.get('previsao_entrega'), data_contrato=request.POST.get('data_contrato'), interessado=inter)
		pro.save()
		return redirect('index')
	interessados = User.objects.all()
	return render(request, 'webapp/new_projeto.html',{'perfil_logado': get_user(request), 'interessados':interessados})

def get_user(request):
	return request.user
def get_atributo(request, id):
	atributo = Atributo.objects.get(id=id)
	return render(request, 'webapp/atributo.html',{'perfil_logado': get_user(request),'atributo':atributo})
def add_membro(request):
	if request.method == 'POST':
		proje = Projeto.objects.get(id=request.POST.get('projeto'))
		mem = User.objects.get(id=request.POST.get('membro'))
		proje.colaboradores.add(mem)
		proje.save()
	return redirect('/projeto/'+str(request.POST.get('projeto'))+'/')

def forum(request):
	foruns = ForumPergunta.objects.all()
	return render(request, 'webapp/forum.html',{'perfil_logado': get_user(request),
		'foruns':foruns})

def add_forum(request):
	if request.method == 'POST':
		forum = ForumPergunta(owner=request.user, titulo=request.POST.get('titulo'),
			descricao=request.POST.get('descricao'), aberto=1)
		forum.save()
	return redirect('forum')