# Generated by Django 4.1.4 on 2022-12-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.SmallIntegerField(choices=[(0, '联想'), (1, '惠普')], default=0, verbose_name='品牌'),
        ),
    ]