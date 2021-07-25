from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class DataMercuryV(models.Model):
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.ForeignKey('TreeMenuV', on_delete=models.PROTECT, null=True, db_column='id_tp')

    class Meta:
        # managed = False
        db_table = 'data_mercury_v'


class DataMercuryS(models.Model):
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.ForeignKey('TreeMenuS', on_delete=models.PROTECT, null=True, db_column='id_tp')

    class Meta:
        # managed = False
        db_table = 'data_mercury_s'


class DataMercuryU(models.Model):
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.ForeignKey('TreeMenuU', on_delete=models.PROTECT, null=True, db_column='id_tp')

    class Meta:
        # managed = False
        db_table = 'data_mercury_u'


class DataMercuryZ(models.Model):
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    energy_reset_sum = models.CharField(max_length=100, blank=True, null=True)
    power_sum = models.CharField(max_length=100, blank=True, null=True)
    energy_day_start = models.CharField(max_length=100, blank=True, null=True)
    energy_day = models.CharField(max_length=100, blank=True, null=True)
    power_day = models.CharField(max_length=100, blank=True, null=True)
    error = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    id_tp = models.ForeignKey('TreeMenuZ', on_delete=models.PROTECT, null=True, db_column='id_tp')

    class Meta:
        # managed = False
        db_table = 'data_mercury_z'


class DeviceMercuryS(models.Model):
    ip = models.CharField(max_length=15, blank=False, null=False, default=0)
    port = models.IntegerField(null=False, blank=False, default=0)
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    network_address = models.IntegerField(null=True, blank=True)


    class Meta:
        db_table = 'device_mercury_s'


class DeviceMercuryU(models.Model):
    ip = models.CharField(max_length=15, blank=False, null=False, default=0)
    port = models.IntegerField(null=False, blank=False, default=0)
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    network_address = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'device_mercury_u'


class DeviceMercuryV(models.Model):
    ip = models.CharField(max_length=15, blank=False, null=False, default=0)
    port = models.IntegerField(null=False, blank=False, default=0)
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    network_address = models.IntegerField(null=True, blank=True)


    class Meta:
        db_table = 'device_mercury_v'


class DeviceMercuryZ(models.Model):
    ip = models.CharField(max_length=15, blank=False, null=False, default=0)
    port = models.IntegerField(null=False, blank=False, default=0)
    serial_number = models.IntegerField(null=False, blank=False, default=0)
    network_address = models.IntegerField(null=True, blank=True)


    class Meta:
        db_table = 'device_mercury_z'


class TreeMenuV(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    device = models.ForeignKey('DeviceMercuryV', on_delete=models.CASCADE, null=True)
    type_connection = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class MPTTmeta:
        order_insertion_by = ['name']


class TreeMenuZ(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    device = models.ForeignKey('DeviceMercuryZ', on_delete=models.CASCADE, null=True)
    type_connection = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class MPTTmeta:
        order_insertion_by = ['name']


class TreeMenuS(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    device = models.ForeignKey('DeviceMercuryS', on_delete=models.CASCADE, null=True)
    type_connection = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class MPTTmeta:
        order_insertion_by = ['name']


class TreeMenuU(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    device = models.ForeignKey('DeviceMercuryU', on_delete=models.CASCADE, null=True)
    type_connection = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class MPTTmeta:
        order_insertion_by = ['name']
