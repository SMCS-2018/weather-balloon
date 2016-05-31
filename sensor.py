import serial
from picamera import PiCamera

class USBDevice():
    def __init__(self: USBDevice, tag: str):
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
                    break

class GeigerCounter(USBDevice):
    def __init__(self: GeigerCounter, tag: str):
        self.BAUDRATE = 9600
        super(GeigerCounter, self).__init__(tag)

    def read_rate(self: GeigerCounter, sample_time: int):
        data = port.read(sample_time * self.BAUDRATE)
        return "".join(bin(i)[2:] for i in data).count("1") / sample_time

class CameraWrapper(PiCamera):
    def __init__(self: CameraWrapper):
        self.pictures_taken = 0
        self.videos_taken = 0
        super(CameraWrapper, self).__init__()
            
    def capture(self: CameraWrapper):
        super(CameraWrapper, self).capture('image' + str(pictures_taken) + '.jpg')
        self.pictures_taken += 1
            
    def start_recording(self: CameraWrapper):
        super(CameraWrapper, self).start_recording('video' + str(videos_taken) + '.h264')
        self.videos_taken += 1
