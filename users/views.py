from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.views import View
from django.contrib import messages, auth
from video_app.models import Video
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profile, Section
from PIL import Image

# Create your views here.
class HomeView(TemplateView):
    template_name: str = "base/base_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video'] = Video.objects.all()[:5]
        return context

class LoginView(View):
    
    def post(self, request):
        #username, password = itemgetter('username', 'password')(data)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(dir(request))
        print(dir(request.POST))
        print(request.POST.dict())
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            #print('login')
            auth.login(request, user)
            return redirect('dashboard')
        return redirect('home')

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')

class ProfileView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Profile
    template_name: str = 'learn/profile_detail.html'
    #slug_url_kwarg: str = 'username'
    #slug_field: str = 'username'
    context_object_name = 'profile'
    login_url = 'home'

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.request.user.pk)
        context['profile'] = user.profile
        return context'''

    def test_func(self):
        if self.request.user.username != self.kwargs.get('username'):
            return False
        return True

    def get_object(self, queryset = None):
        user = User.objects.get(pk=self.request.user.pk)
        profile = self.model.objects.get(user=user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['sections']= profile.section.all()
        return context

    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        image = request.FILES['image']
        #print(request.FILES['image'])
        user = get_object_or_404(User, pk=self.request.user.pk)
        profile = self.model.objects.get(user=user)
        if self.request.user.username != username:
            user.username = username
            user.email = email
            user.save()
        if self.request.user.profile.image != image:
            profile.image = image
            profile.save()
        return redirect('dashboard')

class SectionView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Profile
    template_name: str = 'learn/section_detail.html'
    context_object_name = 'sections'
    login_url = 'home'

    def get_object(self, queryset = None):
        user = User.objects.get(pk=self.request.user.pk)
        sections = self.model.objects.get(user=user).section.all()
        return sections

    def test_func(self):
        if self.request.user.username != self.kwargs.get('username'):
            return False
        return True


'''class TestView(View):
    def get(self, request):
        return render(request, 'testfile.html')

    def post(self, request):
        print(request.FILES)
        im = Image.open(request.FILES['image'])
        im.show()
        return redirect('testing')'''