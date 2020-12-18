import pol_CTRL
import time

#set_pol(chan, pol)
#number = 670
number = 50
for x in range (1,76):
    pol_CTRL.set_pol(0,x*2)
    for y in range (1,76):
        pol_CTRL.set_pol(1,y*2)
        #time.sleep(0.001)
        for z in range (1,76):
            pol_CTRL.set_pol(2,z*2)
            time.sleep(0.001)
    #pol_CTRL.set_pol(2,x*10)
    #pol_CTRL.set_pol(3,x*10)
    #pol_CTRL.set_pol(0,x*10)
    #time.sleep(0.05)
    print(x)
pol_CTRL.closeGPIO()