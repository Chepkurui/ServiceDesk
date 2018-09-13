from django.urls import path

from . import views

app_name = 'engineer'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:department_id>/', views.projects, name='projects'),
    #path('projects/<int:project_id>/', views.project, name='project'),
    #path('<int:stage_id>/results/', views.tasks, name='tasks'),
    #path('<int:task_id>/vote/', views.issues, name='issues'),
    #path('<int:issue_id>/vote/', views.issue, name='issue'),

    #Test
    path('', views.index, name='dashboard'),
    path('ongoingprojects/', views.ongoingprojects, name='ongoingprojects'),
    path('previousprojects/', views.previousprojects, name='previousprojects'),
    path('milestones/', views.milestones, name='milestones'),
    path('incidents/', views.incidents, name='incidents'),
    #path('<int:department_id>/', views.testprojects, name='testprojects'),
    #path('projects/<int:project_id>/', views.testproject, name='testproject'),
    #path('tasks/', views.testtasks, name='testtasks'),
    #path('issues/', views.testissues, name='testissues'),
]