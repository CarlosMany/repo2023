from django import forms
from .models import Tarea, Tarea2

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['tarea']

class Tarea2Form(forms.ModelForm):

    class Meta:
        model = Tarea2
        fields = ['tarea']