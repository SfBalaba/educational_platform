from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from user.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('users/', include('user.urls')),
    path('', include('main.urls')),
]
