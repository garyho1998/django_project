# Generated by Django 3.0.5 on 2020-04-07 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20200407_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='patient',
            new_name='Patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='CaseNumber',
            field=models.CharField(default=-1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='Address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='Detail',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Patient'),
        ),
    ]
