# Generated by Django 2.2.2 on 2019-06-16 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('shortenUrl', models.CharField(max_length=50)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]