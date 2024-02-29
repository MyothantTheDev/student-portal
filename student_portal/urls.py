from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name='accountapp'),
    path('quiz/', include('Quiz.urls'), name='quizes'),
    path('learn-manage/',include('learn_manage.urls'), name='learningapp')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)