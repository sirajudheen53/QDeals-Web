# Generated by Django 2.0 on 2018-06-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_auto_20180610_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='deal',
            name='nubmer_of_peoples_bought',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deal',
            name='number_of_peoples_viewed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deal',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]