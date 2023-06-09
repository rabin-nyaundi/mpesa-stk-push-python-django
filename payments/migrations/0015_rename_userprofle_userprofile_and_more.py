# Generated by Django 4.1.6 on 2023-03-18 09:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("payments", "0014_userprofle"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UserProfle",
            new_name="UserProfile",
        ),
        migrations.AlterModelOptions(
            name="mpesapayment",
            options={"verbose_name_plural": "Mpesa Payments"},
        ),
        migrations.AlterModelOptions(
            name="userprofile",
            options={"verbose_name_plural": "User Profile"},
        ),
    ]
