# Generated by Django 2.2.4 on 2019-11-24 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersApp', '0003_auto_20191124_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cloth',
            new_name='type_of_cloth',
        ),
    ]
