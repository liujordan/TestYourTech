# Generated by Django 2.0.2 on 2018-02-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestYourTech', '0003_auto_20180203_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selector',
            name='selector_type',
            field=models.CharField(choices=[('id', 'ID'), ('css_selector', 'CSS_SELECTOR'), ('xpath', 'XPATH'), ('string', 'STRING')], max_length=256),
        ),
    ]