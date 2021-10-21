# Generated by Django 3.2.7 on 2021-10-19 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_password'),
        ('ctfs', '0005_ctf_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctf',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
