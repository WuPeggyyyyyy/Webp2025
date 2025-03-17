from django.urls import path
from . import views
from .views import course_list, add_course

urlpatterns = [
    #path('', views.HelloApiView.as_view(), name='index'),
    #path('', views.myhello_api, name='index')
    #path('add', views.add_post, name='add_post'),
    #path('list', views.list_post, name='list_post'),
    #path('users', views.list_users, name='list_users'),
    path('courselist', views.course_list, name='course_list'),
    path('addcourse', views.add_course, name='add_course'),
]
