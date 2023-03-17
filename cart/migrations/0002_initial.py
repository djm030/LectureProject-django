
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [

        ("lectures", "0001_initial"),
        ("cart", "0001_initial"),

    ]

    operations = [
        migrations.AddField(
            model_name="numcart",
            name="lecture",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to="lectures.lecture",
            ),
        ),
    ]
