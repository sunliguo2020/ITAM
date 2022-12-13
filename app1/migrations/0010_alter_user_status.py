# Generated by Django 4.1.4 on 2022-12-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(choices=[(None, '请选择'), (0, '正常'), (1, '失效')], default=None, verbose_name='状态'),
        ),
    ]
