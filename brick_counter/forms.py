from django.forms import ModelForm

from .models import House, Task


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ('address', 'year_of_construction')


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('number_of_bricks', 'date_and_time')
