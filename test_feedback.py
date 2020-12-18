import pol_CTRL
import time
import fine_feedback


from ThorlabsPM100 import ThorlabsPM100, USBTMC
inst = USBTMC(device="/dev/usbtmc0")
power_meter = ThorlabsPM100(inst=inst)
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import unravel_index



# P = []

pol_CTRL.initgpio()
total_range = 100
voltage_step = 20
x_init = 0
y_init = 0
z_init = 0
P_x = []
P_y = []
P_z = []
P = np.zeros((total_range,total_range))
rows,columns = (total_range,total_range)
# P = [[]*columns]*rows
for x in range(total_range):
    col = []
    print(x)
    pol_CTRL.set_pol(0,x*voltage_step)
    for y in range(total_range):
        pol_CTRL.set_pol(1,y*voltage_step)
        a=power_meter.read
        col.append(a)
        P_x.append(x*voltage_step)
        P_y.append(y*voltage_step)
        P_z.append(a)
        P[x,y] = a
#         for z in range(total_range):
#             pol_CTRL.set_pol(2,z)
#         P.append(power_meter.read)
#     P.append(col)
#     time.sleep(0.1)
#     P.append(power_meter.read)
# max_index = P.index(max(P))
# print(P.index(max(P)))
# x_volt = (len(P)//max_index)*voltage_step
# y_volt = (len(P)%max_index)*voltage_step
# pol_CTRL.set_pol(0,x_volt)
# pol_CTRL.set_pol(1,y_volt)
(x_max,y_max) = unravel_index(P.argmax(), P.shape)
pol_CTRL.set_pol(0,int((x_max-1)*voltage_step))
pol_CTRL.set_pol(1,int((y_max-1)*voltage_step))
fine_feedback.finer_feedback(int((x_max-1)*voltage_step),int((y_max-1)*voltage_step),30)

pol_CTRL.closeGPIO()
fig, axs = plt.subplots(1,1,num="10")
# print('I am here')
x = np.arange(0,voltage_step*total_range,voltage_step)
y = np.arange(0,voltage_step*total_range,voltage_step)

xs, ys = np.meshgrid(x, y)
# z = calculate_R(xs, ys)
# zs = xs**2 + ys**2

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xs, ys, P,  cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.show()
        
    