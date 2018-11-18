from django.urls import path
from . import views
urlpatterns = [
    path('choinka', views.choinka, name='choinka'),
path('', views.post_list, name='post_list'),
path('post/new', views.post_new, name='post_new'),
]
