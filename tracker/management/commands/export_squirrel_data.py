import csv
import sys
from django.core.management.base import BaseCommand
from tracker.models import Squirrel

class Command(BaseCommand):
    help = 'Export the squirrel data to a csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **kwargs):
        path = kwargs['file_path']
        fields = [a.name for a in Squirrel._meta.fields]
        
        with open(path, 'w') as a:
            writer = csv.writer(a)
            writer.writerow(fields)
            for item in Squirrel.objects.all():
                writer.writerow(str(getattr(item, b.name)) for b in Squirrel._meta.fields)

        a.close()

