# Generated by Django 5.1.6 on 2025-02-23 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inuamkulimaApp', '0009_alter_consultationrequest_consultation_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='consultation_type',
            field=models.CharField(choices=[('phone', 'Phone Consultation'), ('video', 'Video Call Consultation'), ('in-person', 'In-person Consultation')], max_length=20),
        ),
    ]
