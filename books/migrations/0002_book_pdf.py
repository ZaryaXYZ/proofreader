# Generated by Django 4.1 on 2023-07-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="pdf",
            field=models.FileField(blank=True, null=True, upload_to="pdfs/"),
        ),
    ]
