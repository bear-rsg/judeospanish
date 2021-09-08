# Generated by Django 3.2.7 on 2021-09-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0003_story_audio_player_embed_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participationactivity',
            options={'verbose_name_plural': 'Participation Activities'},
        ),
        migrations.AddField(
            model_name='participant',
            name='languages_other',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='knowledge_of_judeospanish',
            field=models.CharField(blank=True, choices=[('NTV', 'I learned Judeo-Spanish in childhood as a first (native) /home language'), ('LTR', 'I learned/studied Judeo-Spanish later in life as an additional (non-native) language'), ('NVR', "I don't know Judeo-Spanish")], max_length=3, null=True),
        ),
    ]
