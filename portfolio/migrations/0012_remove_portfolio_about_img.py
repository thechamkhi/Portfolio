# Generated by Django 4.2.6 on 2023-11-08 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_portfolio_about_portfolio_about_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='about_img',
        ),
    ]
