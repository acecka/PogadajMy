# Generated by Django 4.2.1 on 2023-06-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pogadaj", "0004_rename_first_name_client_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="phone_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="therapist",
            name="phone_number",
            field=models.IntegerField(null=True),
        ),
    ]
