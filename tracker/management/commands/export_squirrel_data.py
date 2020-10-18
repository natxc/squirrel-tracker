import csv
from django.core.management.base import BaseCommand
from tracker.models import Squirrel

class Command(BaseCommand):
    help = 'Export the squirrel data to a csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        fields = Squirrel._meta.fields
        with open(file_path, 'w') as raw_data:
            writer = csv.writer(raw_data)
            for item in Squirrel.items.all():
                row = []
                for field in fields:
                    row.append(getattr(item, field.name))
                writer.writerow(row)
