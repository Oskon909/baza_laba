# Generated by Django 4.1 on 2022-08-23 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("oskon", "0002_category_city_phonenumber_post_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                    "choice",
                    models.CharField(
                        choices=[
                            ("VIP", "VIP"),
                            ("ordinary", "ordinary"),
                            ("urgent", "urgent"),
                        ],
                        default=("ordinary", "ordinary"),
                        max_length=100,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("end_date", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Subscription_Post",
                        to="oskon.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="products/%Y/%m/%d",
                        verbose_name="Фотография",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Image_Post",
                        to="oskon.post",
                    ),
                ),
            ],
        ),
    ]
