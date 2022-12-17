# Generated by Django 4.1.4 on 2022-12-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_computer_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(max_length=16, verbose_name='IP地址')),
                ('mac_addr', models.CharField(max_length=14, verbose_name='MAC地址')),
                ('interface', models.CharField(max_length=16, verbose_name='接口')),
                ('cap_datetime', models.DateTimeField(verbose_name='采集时间')),
            ],
        ),
    ]
