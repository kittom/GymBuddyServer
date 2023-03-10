# Generated by Django 4.1.7 on 2023-03-08 14:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import gymbuddyapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
            ],
            options={"db_table": "accounts",},
        ),
        migrations.CreateModel(
            name="Workout",
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
                ("startTime", models.DateTimeField()),
                ("endTime", models.DateTimeField()),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gymbuddyapi.account",
                    ),
                ),
            ],
            options={"db_table": "workouts",},
        ),
        migrations.CreateModel(
            name="Post",
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
                ("post_datetime", models.DateTimeField()),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=500)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gymbuddyapi.account",
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gymbuddyapi.workout",
                    ),
                ),
            ],
            options={"db_table": "posts",},
        ),
        migrations.CreateModel(
            name="Like",
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
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gymbuddyapi.account",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gymbuddyapi.post",
                    ),
                ),
            ],
            options={"db_table": "likes",},
        ),
        migrations.CreateModel(
            name="Friend",
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
                ("accepted", models.BooleanField()),
                (
                    "account1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_sent",
                        to="gymbuddyapi.account",
                    ),
                ),
                (
                    "account2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_received",
                        to="gymbuddyapi.account",
                    ),
                ),
            ],
            options={"db_table": "friends",},
        ),
        migrations.CreateModel(
            name="Exercise",
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
                ("type", models.CharField(max_length=30)),
                ("datetime", models.DateTimeField()),
                (
                    "file",
                    models.FileField(
                        null=True,
                        upload_to=gymbuddyapi.models.get_file_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
                            )
                        ],
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gymbuddyapi.account",
                    ),
                ),
            ],
            options={"db_table": "exercises",},
        ),
        migrations.AddConstraint(
            model_name="account",
            constraint=models.UniqueConstraint(
                models.OrderBy(
                    django.db.models.functions.text.Lower("username"), descending=True
                ),
                name="unique_username",
            ),
        ),
        migrations.AddConstraint(
            model_name="account",
            constraint=models.UniqueConstraint(
                models.OrderBy(
                    django.db.models.functions.text.Lower("email"), descending=True
                ),
                name="unique_email",
            ),
        ),
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(
                fields=("account", "post"), name="unique_like"
            ),
        ),
        migrations.AddConstraint(
            model_name="friend",
            constraint=models.UniqueConstraint(
                fields=("account1", "account2"), name="unique_friend"
            ),
        ),
    ]
