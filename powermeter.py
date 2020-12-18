#from VapScanFunc import *
#import pymysql
import pyvisa as pyvisa
import socket
import time
import math
from ThorlabsPM100 import ThorlabsPM100, USBTMC
import matplotlib.pyplot as plt
import matplotlib as mpl

VISAInstance=pyvisa.ResourceManager()
VISAInstance.list_resources()
print(VISAInstance)
resourceName='USB0::1313::8078::P0023142::0::INSTR'
inst=VISAInstance.open_resource(resourceName)
print(inst.ask("*IDN?"))
powermeter = ThorlabsPM100(inst=inst)