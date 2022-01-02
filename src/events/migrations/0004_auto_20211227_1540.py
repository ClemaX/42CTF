# Generated by Django 3.1.5 on 2021-12-27 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_auto_20211019_1519'),
    ]

    operations = [
        migrations.RenameModel('Scores', 'EventPlayer'),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('size', models.PositiveIntegerField(default=1)),
                ('score', models.PositiveIntegerField(db_index=True, default=0)),
                ('last_submission_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Submission Date')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]