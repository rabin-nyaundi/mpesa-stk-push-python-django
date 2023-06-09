# Generated by Django 4.1.6 on 2023-03-14 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0003_payment_delete_mpesapayment"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="response_code",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="response_desc",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="result_code",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="payment",
            name="result_desc",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
