"""Конвертация из 16 -> 10 показаний и мощности"""


class Converted:
    @staticmethod
    def converted_values_to_string(data_byte):
        """Конвертация из 16 -> 10 показаний"""
        values_hex = data_byte[2:3] + data_byte[1:2] + data_byte[4:5] + data_byte[3:4]  #
        values = int.from_bytes(values_hex, byteorder='big')  # перевод из 16 -> 10 целой части
        values = float(values / 1000)
        return str(values)

    @staticmethod
    def converted_power_to_string(data_byte):
        """Конвертация из 16 -> 10 мощности"""
        power_hex = data_byte[10:11] + data_byte[9:10] + data_byte[12:13] + data_byte[11:12]  # реактивная мощность
        power = int.from_bytes(power_hex, byteorder='big')  #
        power = float(power / 1000)
        return str(power)

    @staticmethod
    def str_to_byte(string):
        """перевод из strByte -> Byte"""
        string = string.encode()
        string = string.decode('unicode-escape').encode('ISO-8859-1')
        return string