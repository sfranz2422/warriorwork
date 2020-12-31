from django.urls import path
from . import views

urlpatterns = [
    path('alllessons', views.AllLessons.as_view()),
    path('lessons/<int:pk>', views.LessonRetrieveUpdateDestroy.as_view()),
    path('lessons/subject/', views.Subject.as_view()),
    path('lessons/teacher/', views.Teacher.as_view()),
    path('lessons/week/', views.WeekLesson.as_view()),
    path('lessons/', views.Lessons.as_view()),

]
