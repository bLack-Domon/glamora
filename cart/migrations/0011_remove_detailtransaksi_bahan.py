# Generated by Django 5.0.1 on 2024-06-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_transaksi_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailtransaksi',
            name='bahan',
        ),
    ]