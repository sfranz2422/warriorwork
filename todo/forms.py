# we need our own custom form
# and not a django created one
from django.forms import ModelForm
from django import forms
# from .models import Todo
from .models import Week
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget




class WeekForm(ModelForm):
    class Meta:
        content = forms.CharField(widget=CKEditorWidget())


        model = Week
        fields = ['subject', 'last_name', 'week','monday','tuesday', 'wednesday', 'thursday', 'friday']
