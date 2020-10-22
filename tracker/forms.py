from tracker.models import Squirrel
from django.forms import ModelForm

class SquirrelAddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['Longitude', 'Latitude', 'Unique_Squirrel_ID', 'Shift', 'Date', 'Age', 'Primary_Fur_Color', 'Location', 'Specific_Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other_Activities',
                  'Kuks', 'Quaas', 'Moans', 'Tail_flags', 'Tail_twitches', 'Approaches', 'Indifferent', 'Runs_from']

