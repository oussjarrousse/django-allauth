# Generated by Django 4.2.2 on 2023-06-14 12:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0002_email_max_length"),
    ]

    operations = (
        [
            migrations.AlterUniqueTogether(
                name="emailaddress",
                unique_together={("user", "email")},
            ),
            migrations.AddConstraint(
                model_name="emailaddress",
                constraint=models.UniqueConstraint(
                    condition=models.Q(("verified", True)),
                    fields=["email"],
                    name="unique_verified_email",
                ),
            ),
        ]
        if getattr(settings, "ACCOUNT_UNIQUE_EMAIL", True)
        else []
    )