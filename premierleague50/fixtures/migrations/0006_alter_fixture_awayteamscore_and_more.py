# Generated by Django 5.0.4 on 2024-04-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fixtures", "0005_alter_fixture_awayteamscore_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fixture",
            name="awayTeamScore",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="fixture",
            name="homeTeamScore",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
