# Generated by Django 4.2.13 on 2024-07-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABS', '0004_image_extrauserdet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Driver', 'Driver'), ('Cleaner', 'Cleaner'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse')], default='', max_length=50)),
            ],
            options={
                'db_table': 'Designation',
            },
        ),
    ]
