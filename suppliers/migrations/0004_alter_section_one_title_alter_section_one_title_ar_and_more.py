# Generated by Django 5.0 on 2023-12-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("suppliers", "0003_alter_section_two_reports"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section_one",
            name="title",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="section_one",
            name="title_ar",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="section_two",
            name="title",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="section_two",
            name="title_ar",
            field=models.CharField(max_length=500),
        ),
    ]
