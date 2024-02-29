from django.urls import path
from .views import HomeView, LoginView, LogoutView, ProfileView, SectionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<username>/profile/', ProfileView.as_view(), name='user-profile'),
    path('<username>/classes/', SectionView.as_view(), name='classes'),
    #path('test/', TestView.as_view(), name='testing')
]