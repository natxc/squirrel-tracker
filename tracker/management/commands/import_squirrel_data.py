import csv
from django.core.management.base import BaseCommand
from tracker.models import Squirrel
from datetime import datetime, date

class Command(BaseCommand):
    """
    This command is used to import the 2018 Squirrel Data.
    """

    help = 'This is used to import the data from the 2018 Census CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path')


    def handle(self, *args, **kwargs):
        """
        Calls the function to import the data.
        """
        count=0
        path = kwargs['file_path']
        Squirrel.objects.all().delete()

        with open(path, newline='') as raw_data:
            reader = csv.DictReader(raw_data, 
                    fieldnames = ('X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date', 'Hectare Squirrel Number', 'Age', 'Primary Fur Color', 'Highlight Fur Color', 'Combination of Primary and Highlight Color', 'Color notes', 'Location', 'Above Ground Sighter Measurement','Specific Location', 'Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat Long','Zip Codes','Community Districts','Borough Boundaries','City Council Districts','Police Precincts'))
            headers = next(reader)
        
            for item in reader:


                date_proper = datetime.strptime(item['Date'], '%m%d%Y').date()

                Squirrel.objects.create(
                        Longitude = item['X'],
                        Latitude = item['Y'],
                        Unique_Squirrel_ID = item['Unique Squirrel ID'],
                        Shift = item['Shift'],
                        Date = date_proper,
                        Age = item['Age'],
                        Primary_Fur_Color = item['Primary Fur Color'],
                        Location = item['Location'],
                        Specific_Location = item['Specific Location'],
                        Running = make_bool(item['Running']),
                        Chasing = make_bool(item['Chasing']),
                        Climbing = make_bool(item['Climbing']),
                        Eating = make_bool(item['Eating']),
                        Foraging = make_bool(item['Foraging']),
                        Other_Activities = make_bool(item['Other Activities']),
                        Kuks = make_bool(item['Kuks']),
                        Quaas = make_bool(item['Quaas']),
                        Moans = make_bool(item['Moans']),
                        Tail_flags = make_bool(item['Tail flags']),
                        Tail_twitches = make_bool(item['Tail twitches']),
                        Approaches = make_bool(item['Approaches']),
                        Indifferent = make_bool(item['Indifferent']),
                        Runs_from = make_bool(item['Runs from'])
                        )

                count = count+1


def make_bool(string):
    if(string.lower() == 'true'):
        return True
    else:
        return False



