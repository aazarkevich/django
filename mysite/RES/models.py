from django.db import models


class DataMercuryS(models.Model):
    
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_mercury_s'


class DataMercuryTest(models.Model):
    
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_mercury_test'


class DataMercuryU(models.Model):
    
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_mercury_u'


class DataMercuryV(models.Model):
    
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_mercury_v'


class DataMercuryZ(models.Model):
    
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_mercury_z'


class DeviceMercuryS(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    ip = models.CharField(max_length=15)
    port = models.DecimalField(max_digits=65535, decimal_places=65535)
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    parent_id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_mercury_s'


class DeviceMercuryU(models.Model):
    
    ip = models.CharField(max_length=15, blank=True, null=True)
    port = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    parent_id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_mercury_u'


class DeviceMercuryV(models.Model):
    
    ip = models.CharField(max_length=15, blank=True, null=True)
    port = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    parent_id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_mercury_v'


class DeviceMercuryZ(models.Model):
    
    ip = models.CharField(max_length=15, blank=True, null=True)
    port = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    serial_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    parent_id_tp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_mercury_z'

class TreeDeviceMercuryS(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_device_mercury_s'


class TreeDeviceMercuryU(models.Model):
    
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_device_mercury_u'


class TreeDeviceMercuryV(models.Model):
    
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_device_mercury_v'


class TreeDeviceMercuryZ(models.Model):
    
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_device_mercury_z'



