# Generated by Django 5.2 on 2025-04-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='clipped_coupons',
            field=models.TextField(default='[]'),
        ),
    ]
