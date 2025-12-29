from django.urls import path
from .views import *

app_name = 'topics'

urlpatterns = [
    path('', topics_view, name='list'),
    path('subscribe/<int:id>/', subscribe_view),
    path('unsubscribe/<int:id>/', unsubscribe_view),
    path('create/', create_topic_view),
    path('delete/<int:id>/', delete_topic_view),
]
