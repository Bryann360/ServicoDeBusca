# Generated by Django 3.0.6 on 2020-06-01 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20200531_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco',
        ),
    ]
