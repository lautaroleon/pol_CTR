import pol_CTRL
import time
import pymysql
import pymysql.cursors

# from ThorlabsPM100 import ThorlabsPM100, USBTMC
# inst = USBTMC(device="/dev/usbtmc0")
# power_meter = ThorlabsPM100(inst=inst)
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# import write_file
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import unravel_index
from datetime import datetime

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='hercules',
                             password='Teleport1536!',
                             db='Polarization',
#                              charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
START_TIME = '2020-10-26 10:40:00'
END_TIME = '2020-10-26 17:15:30'
ext_ratio = []
Counts = []
Time = []
i = 0
Total_power = 20.1*10**-3 + 12*10**-6
with connection.cursor() as cur:
    TABLE_NAME = "poltest"
    queryGUI = "SELECT datetime, power  FROM "+TABLE_NAME+" WHERE datetime BETWEEN {ts %s} AND {ts %s}"
    cur.execute(queryGUI, (START_TIME,END_TIME,))
    row = cur.fetchone()
    condition = True
    start = True
    while condition:
        row = cur.fetchone()
        if row is None:
            condition = False
        else:
            a = row['power']
            if start:
#                 Time.append(0)
                start_year, start_month, start_day, start_hour, start_minute, start_second = row['datetime'].year, row['datetime'].month, row['datetime'].day, row['datetime'].hour, row['datetime'].minute, row['datetime'].second
            start = False
            end_hour = row['datetime'].hour
            time_spent  = (row['datetime'].day - start_day)*24 + (row['datetime'].hour - start_hour)*1 + (row['datetime'].minute - start_minute)*1/60 + (row['datetime'].second - start_second)*1/3600
            Counts.append(a)
            Time.append(time_spent)
connection.close()

fig, axs = plt.subplots(1,1, num="2")
axs.set_ylabel(r"Extinction_ratio (dB)")
axs.set_xlabel("Elapsed time (hours)")
for k in Counts:
    ext_ratio.append(-10*np.log10((Total_power - k)/k))
axs.plot(Time,ext_ratio)
axs.grid()
# plt.show()
figname = "Extratio_"+str(start_year)+str(start_month)+str(start_day)+"_"+str(start_hour)+str(end_hour)+".png"
plt.tight_layout()
plt.savefig(figname)
# figname = "Pol_stability"+"_"+str(start_year)+str(start_month)+str(start_day)+".png"
# plt.savefig(figname)


