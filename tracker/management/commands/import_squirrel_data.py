import csv
from django.core.management.base import BaseCommand
from tracker.models import Squirrel

class Command(BaseCommand):
    """
    This command is used to import the 2018 Squirrel Data.
    """

    help = 'This is used to import the data from the 2018 Census CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)


    def handle(self, *args, **kwargs):
        """
        Calls the function to import the data.
        """

        with open(kwargs['file_path']) as raw_data:
            my_reader = csv.DictReader(raw_data)
            data = list(my_reader)
            for item in data:
                Longitude = item['X']
                Latitude = item['Y']
                Unique_Squirrel_ID = item['Unique Squirrel ID']
                Shift = item['Shift']
                Date = item['Date'][4:] + '-' + item['Date'][:2] + '-' + item['Date'][2:4]
                Age = item['Age']
                Primary_Fur_Color = item['Primary Fur Color']
                Location = item['Location']
                Specific_Location = item['Specific Location']
                Running = make_bool(item['Running'])
                Chasing = make_bool(item['Chasing'])
                Climbing = make_bool(item['Climbing'])
                Eating = make_bool(item['Eating'])
                Foraging = make_bool(item['Foraging'])
                Other_Activities = make_bool(item['Other Activities']) 
                Kuks = make_bool(item['Kuks'])
                Quaas = make_bool(item['Quaas']) 
                Moans = make_bool(item['Moans']) 
                Tail_flags = make_bool(item['Tail flags'])
                Tail_twitches = make_bool(item['Tail twitches'])
                Approaches = make_bool(item['Approaches'])
                Indifferent = make_bool(item['Indifferent'])
                Runs_from = make_bool(item['Runs from'])

                mapping = Squirrel(
                        Longitude = Longitude,
                        Latitutde = Latitude,
                        Unique_Squirrel_ID = Unique_Squirrel_ID,
                        Shift = Shift,
                        Date = Date,
                        Age = Age,
                        Primary_Fur_Color = Primary_Fur_Color,
                        Location = Location,
                        Specific_Location = Specific_Location,
                        Running = Running,
                        Chasing = Chasing,
                        Climbing = Climbing,
                        Eating = Eating,
                        Foraging = Foraging,
                        Other_Activities = Other_Activities, 
                        Kuks = Kuks,
                        Quaas = Quaas,
                        Moans = Moans, 
                        Tail_flags = Tail_flags,
                        Tail_twitches = Tail_twitches,
                        Approaches = Approaches,
                        Indifferent = Indifferent,
                        Runs_from = Runs_from
                        )
                mapping.save()

     def make_bool(string):
         if (string.lower()=='true'):
             return True
         else:
             return False



