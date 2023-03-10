# Generated by Django 4.1.1 on 2023-01-19 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("username", models.CharField(max_length=50, verbose_name="お名前")),
                ("height", models.FloatField(default=0, verbose_name="身長")),
                (
                    "weight",
                    models.FloatField(
                        blank=True, default=0, null=True, verbose_name="体重"
                    ),
                ),
                (
                    "bmi",
                    models.FloatField(
                        blank=True, default=0, null=True, verbose_name="BMI"
                    ),
                ),
                (
                    "appr_w",
                    models.FloatField(
                        blank=True, default=0, null=True, verbose_name="適正体重"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="日付"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "memo",
                    models.TextField(
                        blank=True, max_length=1000, null=True, verbose_name="メモ"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="ユーザー",
                    ),
                ),
            ],
            options={
                "db_table": "person",
            },
        ),
    ]
