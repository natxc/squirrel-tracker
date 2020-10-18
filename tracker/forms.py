from tracker.models import Squirrel
from django.forms import ModelForm

class SquirrelAddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

