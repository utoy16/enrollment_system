# Generated by Django 3.1.3 on 2020-11-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201126_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(choices=[('Filipino', 'Filipino'), ('English', 'English'), ('Mathematics', 'Mathematics'), ('Science', 'Science'), ('Araling Panlipunan', 'Araling Panlipunan (AP)'), ('Edukasyon sa Pagpapakatao', 'Edukasyon sa Pagpapakatao (EsP)'), ('Edukasyong Pantahanan at Pangkabuhayan', 'Edukasyong Pantahanan at Pangkabuhayan (EPP)'), ('MAPEH', 'MAPEH'), ('Mother Tongue', 'Mother Tongue')], max_length=255),
        ),
    ]
