from django.urls import path
from .views import topic_list

urlpatterns = [
    path('', topic_list, name='topic_list'),
]
