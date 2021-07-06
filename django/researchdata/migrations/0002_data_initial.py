from django.db import migrations
from researchdata import models


def insert_datause(apps, schema_editor):
    """
    Inserts Data Use objects
    """

    data_uses = ["On this website",
                 "Conferences",
                 "Publications",
                 "Social media platforms"]

    for data_use in data_uses:
        models.DataUse(name=data_use).save()


def insert_languages(apps, schema_editor):
    """
    Inserts Language objects
    """

    languages = ["English",
                 "Judeo-Spanish",
                 "French",
                 "Spanish",
                 "Turkish",
                 "Hebrew"]

    for language in languages:
        models.Language(name=language).save()


def insert_participation_activities(apps, schema_editor):
    """
    Inserts ParticipationActivity objects
    """

    activities = ["Interviews",
                  "Questionnaires",
                  "Events"]

    for activity in activities:
        models.ParticipationActivity(name=activity).save()


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_datause),
        migrations.RunPython(insert_languages),
        migrations.RunPython(insert_participation_activities),
    ]
