from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Topic


@login_required(login_url='auth_user')
def topic_list(request: HttpRequest) -> HttpResponse:
    topics = Topic.objects.all()
    return render(request, 'topics/topic_list.html', {'topics': topics})
