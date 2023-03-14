

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Information",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("loginDate", models.DateTimeField(auto_now=True)),
                ("lectureDate", models.DateTimeField(auto_now=True)),
                ("paymentDate", models.DateTimeField(auto_now=True)),
                ("isWithdrawn", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("Withdrawn_at", models.DateTimeField(auto_now=True)),
                ("sDate", models.DateTimeField(auto_now_add=True)),
                ("situation", models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
