import configparser
import serial
import serial.tools.list_ports
from loguru import logger


def main():
    config = configparser.ConfigParser()
    config.read('settings.conf')
    serial_port = config['DATA']['SERIAL_PORT']
    serial_rate = config['DATA']['SERIAL_RATE']

    logger.add("file_{time}.log")
    logger.debug("We've run reading from serial port")
    logger.debug('SERIAL_RATE is {}', serial_port)
    logger.debug('SERIAL_PORT is {}', serial_rate)
    # logger.debug(serial.tools.list_ports.ListPortInfo)

    ser = serial.Serial(serial_port, serial_rate)

    while True:
        try:
            # using ser.readline() assumes each line contains a single reading
            # sent using Serial.println() on the Arduino
            reading = ser.readline().decode('utf-8')
            # reading is a string...do whatever you want from here
            logger.debug(reading)
            # with open("test_data.csv", "a") as f:
            #     writer = csv.writer(f, delimiter=",")
            #     writer.writerow([time.time(), decoded_bytes])
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break


if __name__ == "__main__":
    main()
