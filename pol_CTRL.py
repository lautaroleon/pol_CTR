#https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")



chn_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
#GPIO.setup(2, GPIO.OUT)
#GPIO.setup(3, GPIO.OUT)

# 2,3,4,5,6,7,8,9,10,11,12,13 data
# 14, 15 channel select
# 16 /cs
# 17 /RW
# 18 reset
# GPIO.output(18, 1)
# GPIO.output(18, 0)
#time.sleep(1)
# GPIO.output(18, 1)
# GPIO.output(17, 1)


#2 RW
#3 CS
#4 reset
#5 A0
#6 A1
#7  -- 18


def initgpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(chn_list, GPIO.OUT)

    GPIO.output(4, 1)
    GPIO.output(4, 0)
    
    GPIO.setwarnings(True)
    
def set_pol(chan, pol):
    if (chan>3) or (chan<0):
        print("please insert channel between 1 and 4")
        return -1
    if (pol>4095) or (pol<0):
        print("please insert a polarization value between 0 and 4095")
        return -1
        
    GPIO.output(2, 0)
    #GPIO.output(16, 0)
    GPIO.output(5, chan & 0b1)
    GPIO.output(6, (chan & 0b10)>>1)
    
    GPIO.output(7, pol & 0b1) 
    GPIO.output(8, (pol & 0b10)>>1)
    GPIO.output(9, (pol & 0b100)>>2)
    GPIO.output(10, (pol & 0b1000)>>3)
    GPIO.output(11, (pol & 0b10000)>>4)
    GPIO.output(12, (pol & 0b100000)>>5)
    GPIO.output(13, (pol & 0b1000000)>>6)
    GPIO.output(14, (pol & 0b10000000)>>7)
    GPIO.output(15, (pol & 0b100000000)>>8)
    GPIO.output(16, (pol & 0b1000000000)>>9)
    GPIO.output(17, (pol & 0b10000000000)>>10)
    GPIO.output(18, (pol & 0b100000000000)>>11)
    
    #GPIO.output(2, chan & 0b1)
    
   
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(2, 1)

    #time.sleep(0.0002)
    #print(pol & 0b1)
    #print((pol & 0b10)>>1)
    #print((pol & 0b100)>>2)
    #print((pol & 0b1000)>>3)
   # print((pol & 0b10000)>>4)
    #print((pol & 0b100000)>>5)
    #print((pol & 0b1000000)>>6)
   # print((pol & 0b10000000)>>7)
   # print((pol & 0b100000000)>>8)
    #print((pol & 0b1000000000)>>9)
    #print((pol & 0b10000000000)>>10)
   # print((pol & 0b100000000000)>>11)
    #
    
    
    
def closeGPIO():
    GPIO.cleanup()
    
