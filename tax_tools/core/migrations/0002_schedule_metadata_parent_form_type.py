# Generated by Django 2.0.6 on 2018-07-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule_metadata',
            name='parent_form_type',
            field=models.ManyToManyField(null=True, to='core.Schedule_Metadata'),
        ),
    ]
