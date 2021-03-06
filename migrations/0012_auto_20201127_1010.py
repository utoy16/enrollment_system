# Generated by Django 3.1.3 on 2020-11-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201127_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_no',
            field=models.IntegerField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Parents/Guardian Name'),
        ),
    ]
