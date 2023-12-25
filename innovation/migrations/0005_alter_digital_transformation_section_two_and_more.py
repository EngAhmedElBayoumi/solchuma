# Generated by Django 5.0 on 2023-12-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("innovation", "0004_remove_research_and_development_section_two_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="digital_transformation",
            name="section_two",
            field=models.ManyToManyField(
                blank=True, null=True, to="innovation.section_two"
            ),
        ),
        migrations.AlterField(
            model_name="research_and_development",
            name="section_three",
            field=models.ManyToManyField(
                blank=True, null=True, to="innovation.section_two_research"
            ),
        ),
        migrations.AlterField(
            model_name="research_and_development",
            name="section_two",
            field=models.ManyToManyField(
                blank=True, null=True, to="innovation.section_four_research"
            ),
        ),
    ]
