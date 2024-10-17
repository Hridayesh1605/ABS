# Generated by Django 4.2.13 on 2024-07-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABS', '0007_ambulance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('Addhar', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]
