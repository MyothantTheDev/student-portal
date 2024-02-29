from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Grade, Question, Answer, NoticeBoard
from users.models import Profile

# Create your views here.
class HomeView(LoginRequiredMixin,View):
    login_url = 'home'
    def get(self, request):
        user = User.objects.get(username=request.user)
        profile = Profile.objects.get(user=user)
        notice = []
        sections = profile.section.all()
        for section in sections:
            temp = NoticeBoard.objects.filter(section=section).all()
            notice.append(temp)
        context={'obj': user,'profile': user.profile, 'notices':notice}
        return render(request, template_name='learn/dashboard.html', context=context)

class QuestionView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    login_url = 'home'
    model = Question
    template_name: str = 'learn/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        ans = Answer.objects.filter(user=self.request.user.profile.id).all()
        if not bool(ans):
            questions = self.model.objects.filter(section_id=self.kwargs.get('id'), publish='published')
        else:
            questions = None
        return questions

    def test_func(self):
        if self.request.user.username != self.kwargs.get('username'):
            return False
        return True
    
    def post(self, request, **kwargs):
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')
        questions = []
        try:
            for key in data.keys():
                question = self.model.objects.get(question_field=key)
                questions.append(question)
                question.save()
        
        
            i = 0
            profile = Profile.objects.get(user=self.request.user)
            for value in data.values():
                value = ''.join(value)
                answer = Answer.objects.create(user=profile, 
                        answer_field=value, question=questions[i])
                i += 1
        except:
            pass

        return redirect('dashboard')

class ResultView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    login_url = 'home'
    model = Grade
    context_object_name = 'results'
    template_name: str = 'learn/result_list.html'

    def get_queryset(self):
        result = self.model.objects.filter(user=self.request.user)
        return result

    def test_func(self):
        if self.request.user.username != self.kwargs.get('username'):
            return False
        return True