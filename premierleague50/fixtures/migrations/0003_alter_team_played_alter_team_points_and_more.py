# Generated by Django 5.0.4 on 2024-04-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fixtures", "0002_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="played",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="points",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="team",
            name="ranking",
            field=models.IntegerField(null=True),
        ),
    ]
