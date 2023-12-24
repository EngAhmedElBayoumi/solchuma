# Generated by Django 5.0 on 2023-12-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="affiliates",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("main_image", models.FileField(upload_to="images/")),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
                ("chart_image", models.FileField(upload_to="images/")),
                ("Date", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="board_of_directors",
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
                ("name", models.CharField(max_length=200)),
                ("name_ar", models.CharField(max_length=200)),
                ("image", models.FileField(upload_to="images/")),
                ("job_profile", models.CharField(max_length=200)),
                ("job_profile_ar", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="investments",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("main_image", models.FileField(upload_to="images/")),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
                ("chart_image", models.FileField(upload_to="images/")),
                ("Date", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="management_team",
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
                ("name", models.CharField(max_length=200)),
                ("name_ar", models.CharField(max_length=200)),
                ("image", models.FileField(upload_to="images/")),
                ("job_profile", models.CharField(max_length=200)),
                ("job_profile_ar", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="section_five",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
                ("image", models.FileField(upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="section_four",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
                ("icon", models.FileField(upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="section_one",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
                ("video_link", models.CharField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name="section_three",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="section_two",
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
                ("title", models.CharField(max_length=200)),
                ("title_ar", models.CharField(max_length=200)),
                ("image", models.FileField(upload_to="images/")),
                ("image_ar", models.FileField(upload_to="images/")),
            ],
        ),
    ]
