# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, null=True)
    choice_text = models.CharField(max_length=50)
    votes = models.PositiveIntegerField()

    def __str__(self):
        return self.question.question_text
