# Generated by Django 3.0.6 on 2020-07-25 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_sile',
            new_name='portfolio_site',
        ),
    ]