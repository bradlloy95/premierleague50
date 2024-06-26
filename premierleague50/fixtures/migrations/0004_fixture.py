# Generated by Django 5.0.4 on 2024-04-29 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fixtures", "0003_alter_team_played_alter_team_points_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fixture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("homeTeamScore", models.IntegerField(default=0)),
                ("awayTeamScore", models.IntegerField(default=0)),
                ("fulltime", models.BooleanField()),
                ("date", models.DateField()),
                (
                    "awayTeam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="awayTeam",
                        to="fixtures.team",
                    ),
                ),
                (
                    "homeTeam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="homeTeam",
                        to="fixtures.team",
                    ),
                ),
            ],
        ),
    ]
