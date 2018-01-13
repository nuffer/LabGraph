from serial import Serial as BaseSerial
import serial as base_serial
import sys
import glob

class Serial(BaseSerial):

    def __init__(self,port, baudrate):
        BaseSerial.__init__(self)
        self._baudrate = baudrate
        self.setPort(port)
        pass

    def write_line(self, string):
        string = string + '\n'
        data = string.encode('utf-8')
        self.write(data)

    # read line
    def read_line(self):
        line = self.readline()
        if line != b'':
            return line.decode("utf-8")
        else:
            return None

    # read multi line
    def read_lines(self):
        lines = []
        while True:
            line = self.readline()
            if line != b'':
                lines.append(line.decode("utf-8"))
            else:
                return lines


def list_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = base_serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, base_serial.SerialException):
            pass
    return result