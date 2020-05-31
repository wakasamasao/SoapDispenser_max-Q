import video,time
from Maix import GPIO
from board import board_info
from fpioa_manager import fm
from utime import sleep
import lcd

AUDIO_PA_EN_PIN = 2

lcd.init(freq=15000000)

# open audio PA
if AUDIO_PA_EN_PIN:
    fm.register(AUDIO_PA_EN_PIN, fm.fpioa.GPIO1, force=True)
    wifi_en=GPIO(GPIO.GPIO1, GPIO.OUT)
    wifi_en.value(1)

fm.register(34,  fm.fpioa.I2S0_OUT_D1, force=True)
fm.register(35,  fm.fpioa.I2S0_SCLK, force=True)
fm.register(33,  fm.fpioa.I2S0_WS, force=True)

fm.register(board_info.D[7],fm.fpioa.GPIO7)
execBtn = GPIO(GPIO.GPIO7,GPIO.IN,GPIO.PULL_UP)

sleep(0.5)

while True:
 if execBtn.value() == 0:
     v = video.open("/sd/badapple_320_240_15fps.avi")
     print(v)
     v.volume(10)
     while True:
         if v.play() == 0:
             print("play end")
             break
     v.__del__()



