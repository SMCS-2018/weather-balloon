import serial
# from picamera import PiCamera

BAUDRATE = 9600
PACKET_SIZE = 8

class USBDevice():
    def __init__(self, tag):
        import re
        import subprocess
        device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb", shell = True).decode('utf-8')
        for i in df.split("\n"):
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo["device"] = "/dev/bus/usb/%s/%s" % (dinfo.pop("bus"), dinfo.pop("device"))
                if dinfo["tag"] == tag:
                    self.port = serial.Serial(dinfo["device"], self.BAUDRATE, timeout = 3.0)
                    return

class GeigerCounter(USBDevice):
    def __init__(self, tag):
        self.BAUDRATE = BAUDRATE
        super(GeigerCounter, self).__init__(tag)

    def read_rate(self, sample_time):
        data = self.port.read(sample_time * self.BAUDRATE)
        return "".join(bin(i)[2:] for i in data).count("1") / sample_time

class USBCommunicator(USBDevice):
    def __init__(self, tag):
        self.BAUDRATE = BAUDRATE
        super(USBCommunicator, self).__init__(tag)

    def send_message(message):
        self.port.write(bytes(message))

    def recieve_message():
        return self.port.read(PACKET_SIZE)

class CameraWrapper(PiCamera):
    def __init__(self):
        self.pictures_taken = 0
        self.videos_taken = 0
        super(CameraWrapper, self).__init__()

    def capture(self):
        super(CameraWrapper, self).capture('out/image' + str(self.pictures_taken) + '.jpg')
        self.pictures_taken += 1

    def start_recording(self):
        super(CameraWrapper, self).start_recording('out/video' + str(self.videos_taken) + '.mp4')
        self.videos_taken += 1
