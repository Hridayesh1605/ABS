# Generated by Django 4.2.13 on 2024-07-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABS', '0005_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='staf_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
