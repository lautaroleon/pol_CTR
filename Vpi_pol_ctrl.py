import pol_CTRL
import time


from ThorlabsPM100 import ThorlabsPM100, USBTMC
inst = USBTMC(device="/dev/usbtmc0")
power_meter = ThorlabsPM100(inst=inst)

import matplotlib.pyplot as plt
import matplotlib as mpl



P = []

pol_CTRL.initgpio()

#set_pol(chan, pol)
#number = 670
pol_CTRL.set_pol(1,0)
pol_CTRL.set_pol(2,0)
pol_CTRL.set_pol(3,0)
number = 50
for x in range (1,2000):
   
    pol_CTRL.set_pol(0,x)
#     time.sleep(0.1)
#     pol_CTRL.set_pol(1,x)
#     time.sleep(0.1)
#     pol_CTRL.set_pol(2,x)
#     time.sleep(0.1)
#     pol_CTRL.set_pol(3,x)
#     time.sleep(0.1)
    P.append(power_meter.read)
    #pol_CTRL.set_pol(2,x*10)
    #pol_CTRL.set_pol(3,x*10)
    #pol_CTRL.set_pol(0,x*10)
    #time.sleep(0.05)
    print(x)
    
    
pol_CTRL.closeGPIO()
fig, axs = plt.subplots(1,1,num="10")
# print('I am here')
axs.plot(P)
figname="FineScan0.png"
fig.show()