from django.urls import path
from . import views
urlpatterns = [
    path('choinka', views.choinka, name='choinka'),
path('', views.post_list, name='post_list'),
]
