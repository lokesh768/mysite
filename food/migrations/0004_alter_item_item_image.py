# Generated by Django 4.2 on 2024-10-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0003_item_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_image",
            field=models.ImageField(default="coming.jpg", upload_to="item_pictures"),
        ),
    ]
