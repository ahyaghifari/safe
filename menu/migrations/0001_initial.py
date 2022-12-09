# Generated by Django 4.1.3 on 2022-12-07 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kategori",
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
                ("nama", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
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
                ("nama", models.CharField(max_length=100, unique=True)),
                ("gambar", models.URLField()),
                ("deskripsi", models.TextField(null=True)),
                ("harga", models.SmallIntegerField()),
                (
                    "kategori",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="menu.kategori"
                    ),
                ),
            ],
        ),
    ]
