import sensor
import time
cam=sensor.CameraWrapper()
cam.capture()
cam.start_recording()
time.sleep(5)
cam.stop_recording()
