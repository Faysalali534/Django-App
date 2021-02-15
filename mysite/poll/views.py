from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import Question, Choice


# Create your views here.


def index(request):
    questions = Question.objects.order_by('pub_date')
    # template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': questions,
    }
    return render(request, 'poll/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'poll/detail.html', context)
    # return HttpResponse('Hello detail' + question.question_text)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'poll/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {'question': question, 'error_message': "Not selected a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
