from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# versao comentada e a versao feita na mao ja a outra e usando as views genericass do django
"""
def index(request):
    # Pega as 5 perguntas mais recentes e depois indica um nome
    # para se utilizar a variavel no html e por fim renderiza a
    # pagina html requisitada
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # Verifica se o objeti usado existe e depois renderiza na pagina
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Nao foi selecionado uma opcao',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

def dia(request):
    # escreve a palavra azul em um template no polls/dia
    palavra = 'azul'
    return render(request, 'polls/dia.html', {'palavra': palavra})
