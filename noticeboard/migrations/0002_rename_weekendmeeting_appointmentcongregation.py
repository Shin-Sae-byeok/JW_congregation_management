# Generated by Django 4.1.6 on 2023-02-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("noticeboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="WeekendMeeting", new_name="AppointmentCongregation",
        ),
    ]
