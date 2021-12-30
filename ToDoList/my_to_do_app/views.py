from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# 미리 만들어진 model을 가져오도록 합니다. 
from .models import *

# index 페이지로 돌아가기 위한 reverse를 임포트 합니다. 
from django.urls import reverse

# Create your views here.
def index( request ):
  # DB의 내용을 브라우저에 전달하기 위한 코드를 추가
  todos = Todo.objects.all()
  content = {'todos':todos}
  return render( request, 'my_to_do_app/index.html', content)

def createTodo( request ):

  user_input_str = request.POST['todoContent']
  # models.py에서 정의된 클래스를 이용해서 전달받은 값을 DB에 저장 합니다.
  new_todo = Todo( content = user_input_str )
  new_todo.save()

  return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
  # print('요청변수:', request.GET['todoNum'])
  todo = Todo.objects.get(id=request.GET['todoNum'])
  todo.delete()
  return HttpResponseRedirect(reverse('index'))