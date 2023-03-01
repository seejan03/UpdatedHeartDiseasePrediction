# Generated by Django 3.0.2 on 2021-11-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0006_auto_20211125_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='cap',
        ),
        migrations.AddField(
            model_name='prediction',
            name='ca',
            field=models.IntegerField(default=0, verbose_name='ca'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prediction',
            name='thalach',
            field=models.IntegerField(verbose_name='thalch'),
        ),
    ]
