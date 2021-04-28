# Generated by Django 3.2 on 2021-04-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('name', models.CharField(max_length=100)),
                ('password', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
