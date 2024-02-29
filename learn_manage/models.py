from django.db import models
from django.contrib.auth.models import User
from users.models import Profile, Section
from datetime import datetime

# Create your models here.
class Grade(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    listening = models.IntegerField(null=True)
    reading = models.IntegerField(null=True)
    speaking = models.IntegerField(null=True)
    writing = models.IntegerField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f'{self.user}\'s Grade'

class Question(models.Model):
    options = (('unpublished', 'Unpublished'), ('published', 'Published'))
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, null=False)
    question_field = models.TextField(null=False)
    publish = models.CharField(max_length=15,choices=options,default='published')
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question_field


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer_field = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.user} answered {self.answer_field}"


class NoticeBoard(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return f"{self.section} notice"