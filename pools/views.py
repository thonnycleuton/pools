# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

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


def result(request, pk):
    choices = Choice.objects.filter(question_id__exact=pk)
    template_name = 'results.html'
    context = {
        'choices': choices,
    }
    return render(request, template_name, context)


def vote(request, pk):
    choices = Choice.objects.get(pk=pk)
    choices.votes += 1
    choices.save()
    template_name = 'success.html'
    context = {
        'message': 'successfully saved. Thank you.',
    }
    return render(request, template_name, context)


def manage(request, pk):

    question = Question.objects.get(pk=pk)
    template_name = 'admin.html'
    context = {
        'question': question,
    }
    return render(request, template_name, context)

def manage(request, pk):

    question = Question.objects.get(pk=pk)
    choices = Choice.objects.filter(question_id__exact=pk)
    template_name = 'admin.html'
    context = {
        'choices': choices,
        'question': question,
    }
    return render(request, template_name, context)

def remove(request, pk):

    question = Question.objects.get(pk=pk)
    Choice.objects.get(pk=pk).delete()
    return redirect('pools:manage', question.id)

def status(request, pk):

    question = Question.objects.get(pk=pk)
    question.closed = not question.closed
    question.save()
    return redirect('pools:manage', question.id)