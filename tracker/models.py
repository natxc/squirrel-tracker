from django.db import models

class Squirrel(models.Model):
    Latitude = models.FloatField(
            help_text='Latitude',
            null=False,
            blank=False,
            )
   
    Longitude = models.FloatField(
            help_text='Longitude',
            null=False,
            blank=False,
            )
   
    Unique_Squirrel_ID = models.CharField(
            max_length=100,
            help_text='Unique Squirrel ID',
            unique = True,
            )

    PM = 'PM'
    AM = 'AM'
    Shift_Choices = (
            (PM, 'PM'),
            (AM, 'AM'),
            )
    Shift = models.CharField(
            max_length=2,
            choices=Shift_Choices,
            )

    Date = models.DateField(
            help_text='Date Sighted',
            blank=False,
            )

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Age_Choices = (
            (Adult, 'Adult'),
            (Juvenile, 'Juvenile'),
            )
    Age = models.CharField(
            max_length=30,
            choices=Age_Choices,
            help_text='Age of Squirrel',
            )

    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    Primary_Fur_Color_Choices = (
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (Black, 'Black'),
            )
    Primary_Fur_Color = models.CharField(
            max_length = 25,
            choices=Primary_Fur_Color_Choices,
            help_text='Primary Color of Squirrel',
            )

    Ground_plane = 'Ground_Plane'
    Above_ground = 'Above_Ground'
    Location_Choices = (
            (Ground_Plane, 'Ground_Plane'),
            (Above_Ground, 'Above_Ground'),
            )
    Location = models.CharField(
            max_length=40,
            choices=Location_Choices,
            help_text='Location of Squirrel',
            )

    Specific_Location = models.CharField(
            max_length=1000,
            help_text='More specific location of Squirrel',
            blank = True,
            )

    Running = models.BooleanField(
            help_text='Is the Squirrel running',
            default=False,
            )

    Chasing = models.BooleanField(
            help_text='Is the Squirrel chasing',
            default=False,
            )

    Climbing = models.BooleanField(
            help_text='Is the squirrel climbing',
            default=False,
            )

    Eating = models.BooleanField(
            help_text='Is the squirrel eating',
            default=False,
            )

    Foraging = models.BooleanField(
            help_text='Is the squirrel foraging',
            default=False,
            )
    
    Other_Activities = models.CharField(
            max_length=1000,
            help_text='Other activies that the squirrel is doing',
            blank=True,
            )

    Kuks = models.BooleanField(
            help_text='Does the Squirrel Kuk',
            default=False,
            )

    Quaas = models.BooleanField(
            help_text='Does the Squirrel Quaa',
            default=False,
            )

    Moans = models.BooleanField(
            help_text='Does the Squirrel Moan',
            default=False,
            )

    Tail_flags = models.BooleanField(
            help_text='Does the Squirrel have a tail flag',
            default=False,
            )

    Tail_twitches = models.BooleanField(
            help_text='Does the Squirrel tail twitch',
            default=False,
            )

    Approaches = models.BooleanField(
            help_text='Does the Squirrel approach you',
            default=False,
            )

    Indifferent = models.BooleanField(
            help_text='Is the Squirrel indifferent',
            default=False,
            )

    Runs_from = models.BooleanField(
            help_text='Does the Squirrel run from you',
            default=False,
            )

    def __str__(self):
        return self.Unique_Squirrel_ID






    






# Create your models here.
