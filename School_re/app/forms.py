from django.forms import ModelForm
from .models import Mercury

class StudentForm(ModelForm):
    class Meta:
        model = Mercury
        fields = '__all__'