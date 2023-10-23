# Generated by Django 3.2.10 on 2023-18-10 11:09

from django.conf import settings
from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
          ('course_overviews', '0027_courseoverview_subtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUnitTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id' , models.CharField(max_length=255)),
                ('course_id', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('total' , models.IntegerField(default=0))
            ],
        )
    ]









