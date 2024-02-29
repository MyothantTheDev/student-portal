from django.urls import path
from .views import HomeView, QuestionView, ResultView

urlpatterns = [
    path('dashboard/', HomeView.as_view(), name='dashboard'),
    path('<username>/classes/<int:id>/', QuestionView.as_view(), name='question-list'),
    path('<username>/resultboard/', ResultView.as_view(), name='resultboard')
]