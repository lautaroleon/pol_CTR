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

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='hercules',
                             password='Teleport1536!',
                             db='Polarization',
#                              charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
condition = True
while condition:
    with connection.cursor() as cursor:
        a = power_meter.read
        print(a)
        time.sleep(1)
        # Create a new record
        sql = "INSERT INTO `poltest` (`power`, `datetime`) VALUES (%s, %s)"
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
#     string_value = datetime.datetime.ToString("yyyy-MM-dd HH:mm:ss");
        cursor.execute(sql, (a, formatted_date))
# 
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
    connection.commit()

