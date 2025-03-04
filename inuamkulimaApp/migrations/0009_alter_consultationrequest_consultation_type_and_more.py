# Generated by Django 5.1.6 on 2025-02-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inuamkulimaApp', '0008_remove_consultationrequest_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationrequest',
            name='consultation_type',
            field=models.CharField(choices=[('phone', 'Phone Consultation'), ('video', 'Video Call Consultation'), ('in-person', 'In-Person Consultation')], max_length=20),
        ),
        migrations.AlterField(
            model_name='consultationrequest',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='consultationrequest',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
