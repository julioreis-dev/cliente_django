from django.urls import path
from secretaria.views.login import LoginTemplateView

app_name = 'login'

urlpatterns = [path('', LoginTemplateView.as_view(), name='index'),]