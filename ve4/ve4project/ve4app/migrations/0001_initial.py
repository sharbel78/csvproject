# Generated by Django 4.2.6 on 2024-06-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
