# Generated by Django 4.2.7 on 2023-12-08 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_menuitem_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='cost',
        ),
    ]
