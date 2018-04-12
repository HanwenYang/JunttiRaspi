from picamera import PiCamera, Color
from time import sleep
import datetime

camera = PiCamera()

while True:
    try:
        dt = datetime.datetime.now()
        if (dt.strftime('%I%M')=='0743'):
            recording_name = dt.strftime('%b%d')+'_'+dt.strftime('%H%M')
            camera.start_recording(recording_name + '.h264')
            sleep(1980)
            camera.stop_recording()## to play video use omxplayer or MP4Box
            
    except:
        print ("error")
    