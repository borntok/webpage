
from typing import ParamSpecArgs
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import board
from django.urls import reverse

# Create your views here.

def index(request):
    
    rows = board.objects.all()
    content = {'rows':rows}
    return render(request, 'board/list.html', content)

def write(request):
    return render(request, 'board/write.html')


# 데코레이터를 이용해서 로그인이 필요한 함수 정의
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/accounts/signIn/')
def create(request):
  if request.method == 'POST':  
    new = board(
        user = request.user ,
        createDate = request.POST['createDate'],
        subject = request.POST['subject'],
        content = request.POST['content'] 
        )
    new.save()
    
    return HttpResponseRedirect(reverse('list'))
  else:
    return render(request, 'board/write.html')

@login_required(login_url = '/accounts/signIn/')
def delete(request):
    b = board.objects.get(id=request.POST['id'])
    b.delete()
    
    return HttpResponseRedirect(reverse('list'))

@login_required(login_url = '/accounts/signIn/')
def update(request):
    post = board.objects.get(id = request.GET['id'])
    content = {'post': post}
    return render(request, 'board/update.html', content)


from django.contrib import messages
@login_required(login_url = '/accounts/signIn/')
def modify(request):
    
    post = board.objects.get(id=request.POST['id'])
    if request.user != post.user:
        return render(request, 'board/alert.html')
    else :
      post.createDate = request.POST['createDate']
      post.writer = request.POST['user']
      post.subject = request.POST['subject']
      post.content = request.POST['content']
      post.save()
    
      return HttpResponseRedirect(reverse('list'))    

def view(request):
    post = board.objects.get(id = request.GET['id'])
    content = {'post':post}
    return render(request, 'board/view.html', content)