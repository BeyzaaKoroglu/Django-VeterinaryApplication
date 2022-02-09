# Generated by Django 4.0.2 on 2022-02-09 11:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="description",
            field=models.TextField(
                blank=True, max_length=2000, null=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="petowner",
            name="address",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Address"
            ),
        ),
        migrations.AlterField(
            model_name="petowner",
            name="email",
            field=models.EmailField(
                blank=True,
                max_length=254,
                null=True,
                validators=[django.core.validators.EmailValidator()],
                verbose_name="E-mail",
            ),
        ),
    ]
