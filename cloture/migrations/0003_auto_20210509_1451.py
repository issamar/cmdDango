# Generated by Django 3.2 on 2021-05-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloture', '0002_alter_closure_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closure',
            name='money',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='closure',
            name='wasfa',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
