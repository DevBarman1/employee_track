# Generated by Django 5.0.1 on 2024-04-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_App', '0003_rename_firstname_scheduledemoform_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Media/')),
            ],
        ),
    ]
