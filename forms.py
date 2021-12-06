from django import forms
from .models import TaskModel
from .models import FbModel
from django.forms import Textarea

class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ['task']
		widgets = {'task' : forms.Textarea(attrs = {'rows' : 7,'cols' : 24,'style' : 'resize : none'})}
		
class FbForm(forms.ModelForm):
	class Meta:
		model = FbModel
		fields = ['feedback']
		widgets = {
         	   'feedback': Textarea(attrs={'cols': 40, 'rows': 7, 'style' : 'resize : none'}),
       		}