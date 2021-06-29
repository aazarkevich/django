import libscrc
import datetime
from .converted import Converted


class Mercury:
    """
    Формат запрос на взаимодействие с меркурий 230:
    Сетевой адрес(1 байт) + Код запроса(1 байт) + CRC(2 байта)
    """
    COMMANDS_MERCURY = {'autorization': r"\x01\x01\x01\x01\x01\x01\x01\01",  # запрос на авторизацию
                        'energy_reset_and_power_sum': r"\x05\x00\x00",  # запрос на сумму энергии и мощности
                        'energy_day': r"\x05\x40\x00",  # запрос начало тек суток
                        '3': r"\x06\x02\x06\xa6\x10"}

    def __init__(self, serial_number: str, network_address=False):
        """Серийный номер счетчика"""
        # if not isinstance(serial_number, str):
        #     raise TypeError(str(type(serial_number)) + ' can not cast to str ')

        self.serial_number = str(serial_number)
        if network_address:
            self.network_address = network_address
        else:
            network_address = self._serial_number_to_network_adress(serial_number)

        self.network_address_hex = self._converted_decimal_to_hex(network_address)

    def _serial_number_to_network_adress(self, serial_number):
        """Нахождение сетевого адреса счетчика из серийного номера"""
        if len(serial_number) <= 3:
            network_address = serial_number
        elif int(serial_number[-3:]) > 240:
            network_address = serial_number[-2:]
        else:
            network_address = serial_number[-3:]
        return network_address

    def _converted_decimal_to_hex(self, decimal: str):
        if int(decimal) <= 15:
            result = r'\x0' + str(hex(int(decimal)))[2:6]  # перевод серийного номера из 10 -> 16
        else:
            result = r'\x' + str(hex(int(decimal)))[2:6]

        return result

    def _crc(self, command: str):
        """генерация CRC протокола"""
        network_address_byte = Converted.str_to_byte(self.network_address_hex + command)
        crc16 = str(hex(libscrc.modbus(network_address_byte))[2:6])
        if len(crc16) < 4:
            crc16 = '0' + crc16
        query = self.network_address_hex + command + r'\x' + crc16[2:4] + r'\x' + crc16[0:2]
        query_byte = Converted.str_to_byte(query)
        return query_byte

    @property
    def autorization(self):
        """Код запроса для авторизации"""
        return self._crc(self.COMMANDS_MERCURY['autorization'])

    @property
    def energy_reset_and_power_sum(self):
        """Код для запроса на энергию и мощность от сброса"""
        return self._crc(self.COMMANDS_MERCURY['energy_reset_and_power_sum'])

    @property
    def energy_day(self):
        """Код для запроса на энергию и мощность на начало суток"""
        return self._crc(self.COMMANDS_MERCURY['energy_day'])

# mercury = Mercury('123456189')
# print(mercury.energy_reset_sum_and_power_sum)
# print(type(mercury.network_adress))
# print(mercury.COMMANDS_MERCURY['autorization'])
# print(Mercury.str_to_byte(mercury.COMMANDS_MERCURY['autorization']))
# b'\xbd\x01\x01\x01\x01\x01\x01\x01\x01\x1a\xd6'
