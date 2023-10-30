from django.urls import path
from .import  views

urlpatterns = [
   
  
     path('',views.add_task,name='add'),
    path('delete_task/<int:id>/', views.delete, name='delete'),
    path('update_task/<int:id>/', views.update, name='update'),
    path('listviewadd/', views.TaskListView.as_view(), name='adddv'),
    path('detailview/<int:pk>', views.TaskDetailView.as_view(), name='detail'),
    path('updateview/<int:pk>', views.TaskUpdateView.as_view(), name='update'),
    path('deleteview/<int:pk>', views.TaskDeleteView.as_view(), name='deletedv'),
    
    
    

]
