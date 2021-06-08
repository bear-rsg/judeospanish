from django.db import migrations
from researchdata import models


def insert_languages(apps, schema_editor):
    """
    Inserts Language objects

    n:
EnglishJudeo-SpanishFrenchSpanishTurkishHebrew
 Other [fill in]
    """

    languages = ["English",
                 "Judeo-Spanish",
                 "French",
                 "Spanish",
                 "Turkish",
                 "Hebrew"]

    for language in languages:
        models.Language(name=language).save()


def insert_locations(apps, schema_editor):
    """
    Inserts Location objects
    """

    locations = [
        {"name": "Birmingham", "latitude": 1.1, "longitude": 1.2},
        {"name": "New York", "latitude": 1.5, "longitude": 2.3},
    ]

    for location in locations:
        models.Location(
            name=location["name"],
            latitude=location["latitude"],
            longitude=location["longitude"]
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_languages),
        migrations.RunPython(insert_locations),
    ]
