from picamera import PiCamera, Color
from time import sleep
from subprocess import run

## variables
video_name = 'Qualtest' ##Change video name here (ex: 'name')
video_time = 10 ##Change video length here (time in seconds)

## record video
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_recording(video_name + '.h264')
camera.wait_recording(video_time)
camera.stop_recording() ## to play video on raspi use omxplayer + video paths.

## convert .h264 to .mp4 DOES NOT WORK, MUST DO THIS MANUALLY
input_video = ('/home/pi/JunttiRaspi/VideoRecording/' + video_name + '.h264')
output_video = ('/home/pi/JunttiRaspi/VideoRecording/' + video_name + '.mp4')
print ('MP4Box '+ '-add '+ input_video + ' ' + output_video)
run(['MP4Box', '-add', input_video, output_video],shell = True)