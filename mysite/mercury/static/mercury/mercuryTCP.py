import socket
import libscrc
import datetime
from mercury import Mercury
from converted import Converted


class MercuryTCP(Mercury, Converted):
    an_exception = {'7098469': '169', '105334': '134'}

    def __init__(self, serial_number: str, ip: str, port: str, network_address=None):
        super().__init__(serial_number=serial_number, network_address=network_address)
        self.ip = ip
        self.port = int(port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((self.ip, self.port))

    def connect(self):
        # self.autorization
        pass

    def __execute_query(self, query: bytes):
        pass

    # def connect(self, kodZapros):
    #     autoRiz = self.crcProtokol(self.COMMAND_MERCURY[0][1])
    #     if kodZapros == 0:
    #         return self.executeZapros(autoRiz)
    #
    #     if kodZapros == 1:
    #         zapros = self.crcProtokol(self.COMMAND_MERCURY[2][1])
    #         d1 = self.executeZapros(autoRiz) # Ответ на авторизацию
    #         data = self.executeZapros(zapros) # Ответ на показания на текущие сутки
    #         d2 = self.executeZapros(self.crcProtokol(self.COMMAND_MERCURY[1][1])) #ответ на показания от сброса
    #         return self.serial_number, self.energy_reset_sum(d2,0), self.power_sum(d2,0), self.energy_reset_sum(d2,1) - self.energy_reset_sum(data, 1), \
    #                self.energy_reset_sum(data, 1), self.power_sum(data, 1),'-',datetime.datetime.now().strftime("%m-%d-%Y") # '-' - отображение ошибки
    #
    #     if kodZapros == 2:
    #         zaprosStr = self.COMMAND_MERCURY[kodZapros][1]
    #         zapros = self.crcProtokol(zaprosStr)
    #         d1 = self.executeZapros(autoRiz) # Ответ на авторизацию
    #         data = self.executeZapros(zapros) # ответ на запрос показаний в байтах
    #         return self.energy_reset_sum(data, 0), self.power_sum(data, 0)

    # def __strToByte(self, string): # перевод из strByte -> Byte
    #     string = string.encode()
    #     string = string.decode('unicode-escape').encode('ISO-8859-1')
    #     return string
    #
    # def crcProtokol(self, zaprosStr): # CRC протокол
    #     zaprosIdStr = self.id + zaprosStr
    #     zaprosIdByte = self.__strToByte(zaprosIdStr)
    #     crc16 = str(hex(libscrc.modbus(zaprosIdByte))[2:6])
    #     if len(crc16) < 4:
    #         crc16 = '0' + crc16
    #     zaprosIdStr += r'\x' + crc16[2:4] + r'\x' + crc16[0:2]
    #     # print(zaprosIdStr)
    #     zaprosId = self.__strToByte(zaprosIdStr)
    #     return zaprosId

    # def executeZapros(self, autoRiz = 0, zapros = 0): # выполнение запроса
    #     if zapros != 0:
    #         self.__sock.send(zapros)
    #         self.__sock.settimeout(20)
    #         # self.__sock.close()
    #         return self.__sock.recv(1024)
    #     else:
    #         self.__sock.send(autoRiz)
    #         self.__sock.settimeout(20)
    #         # self.__sock.close()
    #         return self.__sock.recv(1024)

    # def energy_reset_sum(self, data_byte, x = 1):
    #     pokazaniya = data_byte[2:3] + data_byte[1:2] + data_byte[4:5] + data_byte[3:4] #
    #     integerPokaz = int.from_bytes(pokazaniya, byteorder='big') # перевод из 16 -> 10 целой части
    #     if x == 1:
    #         pokazFloat = float(integerPokaz / 1000)
    #         return pokazFloat # показания за тек сутки в Int
    #     if x == 0:
    #         pokazFloat = float(integerPokaz / 1000)
    #         pokazStr = str(pokazFloat)#
    #         return pokazStr
    #
    # def power_sum(self, data_byte, x = 1):
    #     power = data_byte[10:11] + data_byte[9:10] + data_byte[12:13] + data_byte[11:12] # реактивная мощность
    #     # powerRez = 0
    #     powerInt = int.from_bytes(power, byteorder='big') #
    #     if x == 1:
    #         powerFloat = float( powerInt / 1000)
    #         return powerFloat # энергия за тек сутки Int
    #     if x == 0: # энергия за тек сутки
    #         powerFloat = float(powerInt / 1000)
    #         powerStr = str(powerFloat)
    #         return powerStr
    #     # print(id)


if __name__ == "__main__":
    mer = MercuryTCP(serial_number='453783', ip='192.168.143.12', port='35485', network_address='83')
    # print(mer.connect(1))
    print(mer.autorization)
    pass
    # print(float(int(rez) / 1000 ))
