# Generated by Django 4.1.4 on 2022-12-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_computer_brand_alter_computer_computer_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='brand',
            field=models.SmallIntegerField(choices=[(0, '联想'), (1, '惠普')], verbose_name='品牌'),
        ),
    ]
