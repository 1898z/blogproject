
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'), #第三个参数的值将作为处理参数的别名
    path('posts/<int:pk>/',views.detail,name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/',views.category,name='category'),
    path('tags/<int:pk>/',views.tag,name='tag')
]
