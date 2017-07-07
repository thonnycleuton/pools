# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from pools.models import Question, Choice


def index(request):
    questions = Question.objects.all().order_by('-pub_date')
    template_name = 'index.html'
    context = {
        'questions': questions
    }
    return render(request, template_name, context)


def question(request, pk):
    question_obj = Question.objects.get(pk=pk)
    choices = Choice.objects.filter(question=question_obj)
    template_name = 'question.html'
    context = {
        'question': question_obj,
        'choices': choices,
    }
    return render(request, template_name, context)
