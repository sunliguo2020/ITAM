# Generated by Django 4.1.4 on 2022-12-15 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer_type',
            field=models.CharField(max_length=16, null=True, verbose_name='型号'),
        ),
    ]