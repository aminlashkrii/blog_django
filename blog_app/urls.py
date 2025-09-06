from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.post_list, name='post_list'),
    path('list/<int:id>', views.post_detail, name='post_detail'),
]