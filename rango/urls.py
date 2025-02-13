from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),       # 访问 /rango/ 时调用 index()
    path('about/', views.about, name='about'), # 访问 /rango/about/ 时调用 about()
]
