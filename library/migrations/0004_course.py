# Generated by Django 5.1 on 2024-09-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_student_stud_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=5)),
            ],
        ),
    ]
