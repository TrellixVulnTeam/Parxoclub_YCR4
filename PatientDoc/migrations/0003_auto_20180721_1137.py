# Generated by Django 2.0.7 on 2018-07-21 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PatientDoc', '0002_doccatsubmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doccatsubmenu',
            name='docCategories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_menu', to='PatientDoc.DocCategories'),
        ),
    ]