# Generated by Django 3.1.3 on 2020-11-28 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201127_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subject'),
        ),
    ]
