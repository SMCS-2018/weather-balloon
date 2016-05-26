import serial

class USBDevice():
    def __init__(self: usb_device, tag: str):
        import re
        import subprocess
        device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb", shell = True)
        for i in df.split("\n"):
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo["device"] = "/dev/bus/usb/%s/%s" % (dinfo.pop("bus"), dinfo.pop("device"))
                if dinfo["tag"] = tag:
                    self.port = serial.Serial(dinfo["device"], self.BAUDRATE, timeout = 3.0)
                    break

class GeigerCounter(USBDevice):
    def __init__(self: geiger_counter, tag: str):
        self.BAUDRATE = 9600
        super(geiger_counter, self).__init__(tag)

    def read_rate(self: geiger_counter, sample_time: int):
        data = port.read(sample_time * self.BAUDRATE)
        return "".join(bin(i)[2:] for i in data).count("1") / sample_time
