# Generated by Django 2.1.3 on 2018-12-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181208_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.BooleanField(max_length=11, verbose_name='联系电话'),
        ),
    ]
