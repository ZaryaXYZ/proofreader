# Generated by Django 4.2.7 on 2023-12-02 15:24

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0003_alter_usersettings_options_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
