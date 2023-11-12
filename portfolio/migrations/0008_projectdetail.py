# Generated by Django 4.2.6 on 2023-11-04 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_portfolio_github_alter_portfolio_linkedin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_description', models.TextField()),
                ('youtube_demo_link', models.URLField()),
                ('code_link', models.URLField()),
                ('live_link', models.URLField()),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]