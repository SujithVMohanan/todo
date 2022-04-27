from django.urls import path
from . import views
app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:t_id>/', views.delete, name='delete'),
    path('update/<int:uid>/', views.update, name='update'),

    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailsView.as_view(), name='details'),
    path('cbvupdat/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
]