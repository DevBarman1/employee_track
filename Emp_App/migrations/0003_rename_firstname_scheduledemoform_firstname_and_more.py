# Generated by Django 5.0.1 on 2024-04-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_App', '0002_scheduledemoform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduledemoform',
            old_name='Firstname',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='scheduledemoform',
            name='lastname',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
