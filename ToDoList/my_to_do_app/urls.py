from django.urls import path, include
# view와 연결
from . import views

urlpatterns = [
    # 해당 url 패턴을 views.py의 index 함수와 연결
    path('', views.index, name='index'),
    
    # createTpd에 대한 URL 요청과 view를 연결해줍니다.
    path('createTodo/', views.createTodo),
    
    path('deleteTodo/', views.deleteTodo)
]
