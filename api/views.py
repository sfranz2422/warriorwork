from rest_framework import generics, permissions
from .serializers import LessonSerializer
from todo.models import Week
from rest_framework import filters




class Lessons(generics.ListAPIView):
    search_fields = ['subject', 'last_name','week']
    filter_backends = (filters.SearchFilter,)
    # permission_class = [permissions.isAuthenticated]
    queryset = Week.objects.all()
    serializer_class = LessonSerializer




class Subject(generics.ListAPIView):

    search_fields = ['subject']
    filter_backends = (filters.SearchFilter,)
    # permission_class = [permissions.isAuthenticated]
    queryset = Week.objects.all()
    serializer_class = LessonSerializer

class Teacher(generics.ListAPIView):

    search_fields = ['last_name']
    filter_backends = (filters.SearchFilter,)
    # permission_class = [permissions.isAuthenticated]
    queryset = Week.objects.all()
    serializer_class = LessonSerializer

class WeekLesson(generics.ListAPIView):

    search_fields = ['week']
    filter_backends = (filters.SearchFilter,)
    # permission_class = [permissions.isAuthenticated]
    queryset = Week.objects.all()
    serializer_class = LessonSerializer



class LessonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Week.objects.filter(user=user)
        # Todo.objects.filter(datecompleted__isnull=False)

class AllLessons(generics.ListAPIView):
    serializer_class = LessonSerializer

    # permission_class = [permissions.isAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        return Week.objects.filter(subject__isnull=False)
