# Generated by Django 3.2 on 2021-05-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloture', '0009_alter_bordereaux_n_brd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bordereaux',
            name='defr',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
