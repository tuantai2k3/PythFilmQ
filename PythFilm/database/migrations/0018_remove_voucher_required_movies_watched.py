# Generated by Django 5.1.2 on 2024-11-12 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_voucher_uservoucher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='required_movies_watched',
        ),
    ]
