# Generated by Django 4.1.7 on 2023-02-24 20:20

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('gymbuddyapi', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='account',
            constraint=models.UniqueConstraint(models.OrderBy(django.db.models.functions.text.Lower('username'), descending=True), name='unique_username'),
        ),
    ]
