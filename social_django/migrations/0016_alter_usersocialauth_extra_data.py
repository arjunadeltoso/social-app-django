# Generated by Django 3.2.25 on 2024-05-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0015_rename_extra_data_new_usersocialauth_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocialauth',
            name='extra_data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
