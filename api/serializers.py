from rest_framework import serializers
from todo.models import Week


class LessonSerializer(serializers.ModelSerializer):
    

    created = serializers.ReadOnlyField()



    class Meta:
        model = Week
        fields = ['id', 'created', 'last_name','subject','week', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
