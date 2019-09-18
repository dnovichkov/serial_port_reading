These project works with Python3.

It's recommended to setup virtual environment. Here are some links:
[https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) and 
[https://virtualenv.pypa.io/en/stable/userguide/](https://docs.python.org/3/library/venv.html)

Example for Windows:

```
python -m venv env
cd env/Scripts
activate.bat
```

Then return to source directory and install necessary modules:

```
cd ../../
pip install -r requirements.txt
```

Congratulations, now it is possible to run script:

```
python main.py
```

It is possible to change some port settings using settings.conf:

 ```
[DATA]
# This port address is for the serial tx/rx pins on the GPIO header
#SERIAL_PORT = /dev/ttyAMA0
SERIAL_PORT = COM1
# Be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
```

If you want to get all ports in your system you can do it by command:

 ```
python -m serial.tools.list_ports -v
 ```
 
Data format from serial port is:
```
Temperature1=56
Temperature2=54
Temperature3=53
```
 
Some code for debug purposes:
```
import serial
ser = serial.Serial('COM2')
ser.write(b'Temperature1=56\nTemperature2=54\n')
ser.write(b'Temperature1=55\nTemperature2=56\n')
ser.write(b'Temperature1=51\nTemperature2=55\n')
ser.write(b'Temperature2=58\nTemperature1=60\n')
ser.close()   
```

If you want to create executable file:
```
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
OR pyinstaller --noconsole main.py
```
