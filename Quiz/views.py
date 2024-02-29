from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Answer, Quiz, Question, Result
from django.http import JsonResponse
import uuid
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name: str = 'quiz/main.html'
    context_object_name = 'quizes'

class QuizDetailView(DetailView):
    model = Quiz
    template_name: str = 'quiz/quiz_detail.html'
    context_object_name = 'quiz'

class QuizDataView(View):
    def get(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        questions = []
        for q in quiz.get_question():
            answers = []
            for a in q.get_answers():
                answers.append(a.text)
            questions.append({str(q): answers})
        return JsonResponse({'data': questions, 'time': quiz.time})

    def is_ajax(self, request):
        return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def post(self, request, pk):
        if self.is_ajax(request):
            questions = []
            data = request.POST
            data_ = dict(data)
            data_.pop('csrfmiddlewaretoken')
            
            for k in data_.keys():
                question = Question.objects.get(text=k)
                questions.append(question)

            quiz = Quiz.objects.get(pk=pk)

            score = 0
            multiplier = 100 / quiz.number_of_questions
            results = []
            correct_answer = None

            for q in questions:
                a_selected = request.POST.get(q.text)

                if a_selected != "":
                    question_answers = Answer.objects.filter(question=q)
                    for a in question_answers:
                        if a_selected == a.text:
                            if a.correct:
                                score += 1
                                correct_answer = a.text
                        else:
                            if a.correct:
                                correct_answer = a.text
                    
                    results.append({str(q): {'correct_answer': correct_answer,'answered': a_selected}})
                else:
                    results.append({str(q): 'not answered'})
            user = str(uuid.uuid4())
            score_ = score * multiplier
            Result.objects.create(quiz=quiz, score=score_, user=user)

            if score_ >= quiz.required_score_to_pass:
                return JsonResponse({'passed': True, 'score': score_, 'results': results, 'id':user})
            else:
                return JsonResponse({'passed': False, 'score': score_, 'results': results, 'id':user})
        return JsonResponse({'text': 'works'})