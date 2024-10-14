# Generated by Django 5.1 on 2024-09-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_delete_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('mentor_name', models.CharField(max_length=225)),
                ('mentor_room_no', models.CharField(default='sk2', max_length=3)),
            ],
        ),
    ]
