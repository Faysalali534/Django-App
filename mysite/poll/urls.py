from django.urls import path
from django.urls import include
from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('results/<int:question_id>', views.results, name='results'),
    path('vote/<int:question_id>', views.vote, name='vote')
]
