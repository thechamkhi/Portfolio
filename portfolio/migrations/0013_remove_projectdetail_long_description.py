# Generated by Django 4.2.6 on 2023-11-08 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_remove_portfolio_about_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetail',
            name='long_description',
        ),
    ]