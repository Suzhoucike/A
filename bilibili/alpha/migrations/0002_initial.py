# Generated by Django 5.0 on 2023-12-20 17:31

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("alpha", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrainingPlan",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                ("name", models.CharField(max_length=32)),
                ("password", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="CourseCategory",
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
                ("name", models.CharField(max_length=255)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="alpha.coursecategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=255, null=True)),
                (
                    "coursecode",
                    models.CharField(default=None, max_length=30, null=True),
                ),
                ("credits", models.CharField(default=None, max_length=5, null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alpha.coursecategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TrainingClass",
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
                ("must", models.BooleanField(null=True)),
                ("semester", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "category_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alpha.coursecategory",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alpha.course",
                    ),
                ),
                (
                    "training_plan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alpha.trainingplan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TrainingCategory",
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
                ("category_id", models.IntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                ("parent", models.IntegerField(blank=True, null=True)),
                ("credits", models.IntegerField(default=0)),
                ("detail", models.TextField(null=True)),
                (
                    "training_plan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alpha.trainingplan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CourseCategory_display",
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
                ("category_id", models.IntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                ("credits", models.IntegerField(default=0)),
                ("detail", models.TextField(null=True)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="alpha.coursecategory_display",
                    ),
                ),
                (
                    "training_plan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="alpha.trainingplan",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
