# Generated by Django 4.2.15 on 2024-08-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0209_user_show_ratings"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="disable_federation",
            field=models.BooleanField(default=False),
        ),
    ]
