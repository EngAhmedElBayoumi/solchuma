# Generated by Django 5.0 on 2023-12-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="images",
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
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="images",
            field=models.ManyToManyField(
                related_name="product_images", to="products.images"
            ),
        ),
    ]
