import serial
import picamera

class USBDevice():
    def __init__(self, tag):
        import re
        import subprocess
        device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb", shell = True)
        df = df.decode('utf-8') #were using python3
        for i in df.split("\n"):
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo["device"] = "/dev/bus/usb/%s/%s" % (dinfo.pop("bus"), dinfo.pop("device"))
                if dinfo["tag"] == tag:
                    self.port = serial.Serial(dinfo["device"], self.BAUDRATE, timeout = 3.0)
                    break

class GeigerCounter(USBDevice):
    def __init__(self, tag):
        self.BAUDRATE = 9600
        super(GeigerCounter, self).__init__(tag)

    def read_rate(self, sample_time):
        data = port.read(sample_time * self.BAUDRATE)
        return "".join(bin(i)[2:] for i in data).count("1") / sample_time

class CameraWrapper:
	def __init__(self):
		self.numPicsTaken=0
		self.numVidsTaken=0
		self.camera=picamera.PiCamera()
	def takePic():
		self.camera.capture('image'+str(numPicsTaken)+'.jpg')
		self.numPicsTaken+=1
	def startVid():
		self.camera.start_recording('video'+str(numVidsTaken)+'.h264')
		self.numVidsTaken+=1
	def stopVid():
		self.camera.stopRecording()


