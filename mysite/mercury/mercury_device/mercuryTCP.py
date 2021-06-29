import socket
from datetime import datetime
from .mercury import Mercury
from .converted import Converted


class MercuryTCP(Mercury):
    an_exception = {'7098469': '169', '105334': '134'}

    def __init__(self, serial_number: str, ip: str, port: str, network_address=None):
        super().__init__(serial_number=serial_number, network_address=network_address)
        self.ip = ip
        self.port = int(port)

    def __connection(self):
        """Открытие соединеня с модемом по ip и порту"""
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((self.ip, self.port))
        return self.__execute_query(self.autorization)

    def __close_connection(self):
        return self.__sock.close()

    def __execute_query(self, query: bytes):
        """Нахождение сетевого адреса счетчика из серийного номера"""
        self.__sock.send(query)
        self.__sock.settimeout(10)
        # self.__sock.close()
        return self.__sock.recv(1024)

    def _values_and_power(self):
        """Отправить запрос на получении энергии и мощности от сброса"""
        try:
            self.__connection()
        except (socket.timeout, ConnectionRefusedError) as Ex:
            self.__energy = 0
            self.__power = 0
            self.__error = Ex
            return
        else:
            self.__error = '-'
        values = self.__execute_query(self.energy_reset_and_power_sum)
        self.__energy = Converted.converted_values_to_string(values)
        self.__power = Converted.converted_power_to_string(values)

    def get_values(self) -> dict:
        """Вернуть полученые значения"""
        self._values_and_power()
        return dict(serial_number=self.serial_number, energy=self.__energy, power=self.__power, error=self.__error,
                    data=datetime.now().strftime("%m-%d-%Y"))


if __name__ == "__main__":
    # mer = MercuryTCP(serial_number='453783', ip='192.168.143.12', port='35485')
    # print(mer.connect(1))
    # print(mer.get_values())
    pass
    # print(float(int(rez) / 1000 ))
