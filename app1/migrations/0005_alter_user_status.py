# Generated by Django 4.1.4 on 2022-12-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_computer_mod_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(choices=[(None, '请选择'), (0, '正常'), (1, '失效')], default=None, null=True, verbose_name='状态'),
        ),
    ]
