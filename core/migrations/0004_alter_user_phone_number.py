# Generated by Django 5.2 on 2025-05-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
