# Generated by Django 3.0.5 on 2020-04-07 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20200407_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Category',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='location',
            name='DateFrom',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='DateTo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='District',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='location',
            name='LocationVisited',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='location',
            name='XCoord',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='YCoord',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DateCaseConfirmed',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DateOfBirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='IdentityDocumentNumber',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]