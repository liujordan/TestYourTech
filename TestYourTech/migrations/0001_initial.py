# Generated by Django 2.0.2 on 2018-02-04 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('action_type', models.CharField(blank=True, choices=[('click', 'CLICK'), ('type', 'TYPE'), ('url', 'GO TO URL'), ('submit', 'SUBMIT')], default='click', max_length=256)),
                ('selector', models.CharField(blank=True, max_length=256)),
                ('value', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('after', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestYourTech.Action')),
                ('this', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current', to='TestYourTech.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('selector', models.CharField(max_length=256)),
                ('value', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='action_link',
            field=models.ManyToManyField(through='TestYourTech.ActionLink', to='TestYourTech.Action'),
        ),
        migrations.AddField(
            model_name='action',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TestYourTech.Result'),
        ),
    ]
