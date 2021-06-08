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


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_languages),
    ]
