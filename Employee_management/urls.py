from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('get/', views.get_data, name='get_data'),
    path('get/<int:id>/', views.get_specific_employee, name='get_specific_employee'),
    path('attendance/mark/<int:id>/<str:status>', views.mark_attendance, name='mark_attendance'),
    path('attendance/get/', views.get_attendance, name='get_attendance'),
    path('attendance/get/<str:dep_name>/',views.get_specificdep_attendance,name='get_specificdep_attendance')
]
