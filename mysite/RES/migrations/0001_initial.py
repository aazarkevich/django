# Generated by Django 3.2 on 2021-05-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataMercuryS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('energy_reset_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('power_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day_start', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day', models.CharField(blank=True, max_length=100, null=True)),
                ('power_day', models.CharField(blank=True, max_length=100, null=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'data_mercury_s',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataMercuryTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('energy_reset_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('power_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day_start', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day', models.CharField(blank=True, max_length=100, null=True)),
                ('power_day', models.CharField(blank=True, max_length=100, null=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'data_mercury_test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataMercuryU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('energy_reset_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('power_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day_start', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day', models.CharField(blank=True, max_length=100, null=True)),
                ('power_day', models.CharField(blank=True, max_length=100, null=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'data_mercury_u',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataMercuryV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('energy_reset_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('power_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day_start', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day', models.CharField(blank=True, max_length=100, null=True)),
                ('power_day', models.CharField(blank=True, max_length=100, null=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),

            ],
            options={
                'db_table': 'data_mercury_v',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataMercuryZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('energy_reset_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('power_sum', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day_start', models.CharField(blank=True, max_length=100, null=True)),
                ('energy_day', models.CharField(blank=True, max_length=100, null=True)),
                ('power_day', models.CharField(blank=True, max_length=100, null=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'data_mercury_z',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceMercuryS',
            fields=[
                ('id', models.DecimalField(decimal_places=65535, max_digits=65535, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=15)),
                ('port', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('parent_id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'device_mercury_s',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceMercuryU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=15, null=True)),
                ('port', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('parent_id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'device_mercury_u',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceMercuryV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=15, null=True)),
                ('port', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('parent_id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'device_mercury_v',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceMercuryZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=15, null=True)),
                ('port', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('serial_number', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('parent_id_tp', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'device_mercury_z',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreeDeviceMercuryS',
            fields=[
                ('id', models.DecimalField(decimal_places=65535, max_digits=65535, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tree_device_mercury_s',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreeDeviceMercuryU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tree_device_mercury_u',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreeDeviceMercuryV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tree_device_mercury_v',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TreeDeviceMercuryZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'tree_device_mercury_z',
                'managed': False,
            },
        ),
    ]
