from django.urls import path
from secretaria.views.views import IndexTemplateView

app_name = 'home'

urlpatterns = [path('', IndexTemplateView.as_view(), name='index'),
               ]