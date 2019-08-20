#import wmi
import random
import psutil
import digital_assistant_funcs



VISUAL_CODE_STUDIO_DIR = ""

ARDUINO_DIR = ""

PYCHARM_DIR = ""





def brightness(voice_note):
	if 'decrease ' in voice_note:
		print('ok listen.......')
		dec = wmi.WMI(namespace='wmi')
		methods = dec.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(30, 0)
	elif 'increase ' in voice_note:
		print('ok listen.......')
		ins = wmi.WMI(namespace='wmi')
		methods = ins.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(100, 0)

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)



# Power Time Convert
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)


def battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    time_left = secs2hours(battery.secsleft)
    digital_assistant_funcs.speak(str(percent))
    if percent < 40 and plugged == False:
        digital_assistant_funcs.speak('sir, please connect charger because i can survive only ' + time_left)
    if percent < 40 and plugged == True:
        digital_assistant_funcs.speak("don't worry,charger is connected")
    else:
        digital_assistant_funcs.speak('no need to connect the charger because i can survive ' + time_left)
