# Generated by Django 3.2.2 on 2021-05-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('experince', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
    ]
