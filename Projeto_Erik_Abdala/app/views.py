from typing import Any
from django.shortcuts import render, get_object_or_404
from . models import *

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import HttpResponseNotFound

from datetime import datetime

# Create your views here.

def area(request):

    areas = {
        'areas':Area.objects.all()
    }

    return render(request, 'exibicao/area.html', areas)

def subarea(request):

    subareas = {
        'subareas':Subarea.objects.all(),
        'areas':Area.objects.all()
    }

    return render(request, 'exibicao/subarea.html', subareas)

def fisico(request):

    fisicos = {
        'fisicos':Fisico.objects.all()
    }

    return render(request, 'exibicao/fisico.html', fisicos)

def invencao(request):

    invencoes = {
        'invencoes':Invencao.objects.all()
    }

    return render(request, 'exibicao/invencao.html', invencoes)

def ocupacao(request):

    ocupacoes = {
        'ocupacoes':Ocupacao.objects.all()
    }

    return render(request, 'exibicao/ocupacao.html', ocupacoes)

def pessoa(request):

    pessoas = {
        'pessoas':Pessoa.objects.all(),
        'alunos':Pessoa.objects.filter(ocupacao__nome = 'Aluno(a)').values(),
        'professores':Pessoa.objects.filter(ocupacao__nome = 'Professor(a)').values(),
    }

    return render(request, 'exibicao/pessoa.html', pessoas)

def questionario(request):

    questionarios = {
        'questionarios':Questionario.objects.all()
    }

    return render(request, 'exibicao/questionario.html', questionarios)

class TopicoListView(ListView):
    
    model = Area

    context_object_name = "areas"

    template_name = "exibicao/topico/topico-list.html"

class TopicoDetailView(DetailView):

    model = Topico

    context_object_name = "topico"

    template_name = "exibicao/topico/topico-detail.html"

class QuestionarioListView(ListView):

    model = Questionario

    context_object_name = "questionarios"

    template_name = "exibicao/questionario/questionario-list.html"

class QuestionarioDetailView(DetailView):

    model = Questionario

    context_object_name = "questionario"

    template_name = "exibicao/questionario/questionario-detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        membros = Pessoa.objects.all()

        context['membros'] = membros

        return context

def submeter_respostas(request, questionario_id):

    questionario = get_object_or_404(Questionario, pk = questionario_id)

    questoes = questionario.questao_set.all()

    if request.method == 'POST':

        pessoa_id = request.POST.get('membro')

        pessoa = get_object_or_404(Pessoa, pk = pessoa_id)

        numero_acertos = 0

        respostas = {}

        for questao in questoes:

            nome_input = f'Q{questao.id}'

            resposta = request.POST.get(nome_input)

            respostas[questao.id] = resposta

            print(f'Resposta correta: {questao.alternativa_correta}, Resposta submetida: {resposta}')

            if resposta == questao.alternativa_correta:

                numero_acertos += 1

        questionario_respondido = QuestionarioRespondido.objects.create(
            questionario = questionario,
            pessoa = pessoa,
            data_realizacao = datetime.now(),
            numero_acertos = numero_acertos,
        )

        questionario_respondido.save()

        respostas_corretas = {}

        for questao in questoes:

            respostas_corretas[questao.id] = questao.alternativa_correta
        
        context = {
            'respostas_corretas': respostas_corretas,
        }

        return render(request, 'exibicao/agradecimento.html', context)
    
    return HttpResponseNotFound('<h1>Página não encontrada</h1>')

def respondido(request):

    respondidos = {
        'respondidos':QuestionarioRespondido.objects.all()
    }

    return render(request, 'exibicao/respondido.html', respondidos)