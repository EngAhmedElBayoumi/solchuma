# Generated by Django 5.0 on 2023-12-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("innovation", "0003_research_and_development_section_two"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="research_and_development",
            name="section_two",
        ),
        migrations.AddField(
            model_name="research_and_development",
            name="section_two",
            field=models.ManyToManyField(to="innovation.section_four_research"),
        ),
    ]
