# Generated by Django 5.0 on 2023-12-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sustainability", "0002_social_section_one_title_social_section_one_title_ar"),
    ]

    operations = [
        migrations.AddField(
            model_name="governance_section_one",
            name="title",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="governance_section_one",
            name="title_ar",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
