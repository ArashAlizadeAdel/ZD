# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys  
import os.path
import time
import datetime
x = os.path.getmtime(r"C:\Users\a.alizadeh\Desktop\x.xlsx")
x = datetime.datetime.utcfromtimestamp(x)
print(type(x))
x = datetime.datetime.strptime(x,'%Y-%m-%d')
#from Script1 import x
#
#x()