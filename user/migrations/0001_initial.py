# Generated by Django 5.0 on 2023-12-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('mobile_no', models.CharField(max_length=10)),
                ('grade', models.IntegerField()),
                ('faculty', models.CharField(max_length=50)),
            ],
        ),
    ]