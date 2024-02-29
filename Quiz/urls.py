from django.urls import path
from .views import QuizListView, QuizDetailView, QuizDataView

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-main'),
    path('<pk>/', QuizDetailView.as_view(), name='quiz-view'),
    path('<pk>/data/', QuizDataView.as_view(), name='quiz-data-view')
]