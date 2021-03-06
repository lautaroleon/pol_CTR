import pol_CTRL
import time
import pymysql
import pymysql.cursors

from ThorlabsPM100 import ThorlabsPM100, USBTMC
inst = USBTMC(device="/dev/usbtmc0")
power_meter = ThorlabsPM100(inst=inst)
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# import write_file
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import unravel_index
from datetime import datetime
# file1 = open('power.txt', 'w')


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='hercules',
                             password='Teleport1536!',
                             db='Polarization',
#                              charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def finer_feedback(x_max,y_max,fine_range):
    condition = True
    while condition:
     
        P = np.zeros((fine_range,fine_range))
        for x in range(fine_range):
            pol_CTRL.set_pol(0,max(int(x + x_max - fine_range/2),0))
            for y in range(fine_range):
                pol_CTRL.set_pol(1,max(int(y + y_max - fine_range/2),0))
                P[x,y] = power_meter.read
        (x_index,y_index) = unravel_index(P.argmax(), P.shape)
    
#     write_file.write_file(str(power_meter.read))
        print(x_index,y_index)
        pol_CTRL.set_pol(0,int((x_index + x_max - fine_range/2)))
        pol_CTRL.set_pol(1,int((y_index + y_max - fine_range/2)))
    
        with connection.cursor() as cursor:
            a = power_meter.read
            # Create a new record
            sql = "INSERT INTO `poltest` (`power`, `datetime`) VALUES (%s, %s)"
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(sql, (a, formatted_date))
# 
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
        connection.commit()
        x_max = int((x_index + x_max - fine_range/2))
        y_max = int((y_index + y_max - fine_range/2))
        
#     with open("mypower_1.txt", "a") as file1:
#         file1.writelines(str(power_meter.read)+'\n')
#         finer_feedback(int((x_index + x_max - fine_range/2)),int((y_index + y_max - fine_range/2)),fine_range)
#     file1.close()
    