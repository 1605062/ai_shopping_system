# Generated by Django 3.2 on 2021-05-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_customeractivity_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeractivity',
            name='count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
