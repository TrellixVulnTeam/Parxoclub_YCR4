# Generated by Django 2.0.7 on 2018-08-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    operations = [
        migrations.AlterField(
            model_name='memberships',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]