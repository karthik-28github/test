# Generated by Django 4.0.1 on 2022-01-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mobilenumber', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('confirmpassword', models.CharField(max_length=20)),
            ],
        ),
    ]
