# Generated by Django 4.1.4 on 2022-12-15 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_computer_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owners', to='app1.user', verbose_name='拥有者'),
        ),
    ]
