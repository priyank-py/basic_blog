# Generated by Django 3.0.2 on 2020-01-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articlereview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
