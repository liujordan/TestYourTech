# Generated by Django 2.0.2 on 2018-02-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestYourTech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='left_pos',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='top_pos',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]