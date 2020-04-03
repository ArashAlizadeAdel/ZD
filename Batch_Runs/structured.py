# -*- coding: utf-8 -*-

print("***Data Cleaning Process For Data of Structured Reports Just Started***")

import pandas as pd
import numpy as np
import os
import sys
import datetime as dt

sys.path.append("D:\AlizadeAdel\Reporting System\script_cleaning")

from raw1 import raw1
from raw2 import raw2
from raw3 import raw3
from raw4 import raw4

Year = str(input("Year : "))
Month = str(input("Month : "))
YM = "-" + Year + "-" + Month

KalaForosh = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Kala-Forosh98.xlsx"
KalaAnbar = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Kala-Anbar98.xlsx"
GoalsCategory = r"D:\AlizadeAdel\Reporting System\data_lookup\GoalsCategory.xlsx"
SaleTurnOver = r"D:\AlizadeAdel\Reporting System\data_raw\structured\AghlamGardesh\2020-02.xlsx"
Invoice_Acc = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Factor-TarikhFactor-HesabDari98.xlsx"
Invoice_Sale = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Factor-TarikhFactor-Forosh98.xlsx"
DateTable = r"D:\AlizadeAdel\Reporting System\data_raw\structured\DateTable.xlsx"
Return = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Aghlam-Bargasht-Az-Forosh98.xlsx"
AghlamTasvie = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Aghlam-Tasvie98.xlsx"
Chek = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Chek98.xlsx"
Moshtari = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Moshtari98.xlsx"

print("***Paths obtained***")

#First data cleaning module
raw1 = raw1(KalaForosh,KalaAnbar,GoalsCategory)
raw1[0].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Product.csv",encoding = "utf-8-sig",index = False)
print("***raw1 part 0 Saved***")
raw1[1].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\ProductCategories.csv",encoding = "utf-8-sig",index = False)
print("***raw1 part 1 Saved***")

#Second one
raw2 = raw2(SaleTurnOver,Invoice_Acc,Invoice_Sale,KalaAnbar,DateTable,Moshtari)
raw2[0].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Dealer.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 0 Saved***")
raw2[1].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Distributer.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 1 Saved***")
raw2[2].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Customer.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 2 Saved***")
raw2[3].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\ReturnCause.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 3 Saved***")
raw2[4].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\DistCenter_Line.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 4 Saved***")
raw2[5].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Invoice{}.csv".format(YM),encoding = "utf-8-sig",index = False)
print("***raw2 part 5 Saved***")
raw2[6].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Invoice_Detail{}.csv".format(YM),encoding = "utf-8-sig",index = False)
print("***raw2 part 6 Saved***")
raw2[7].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Debt.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 7 Saved***")
raw2[8].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\InvoiceAll.csv",encoding = "utf-8-sig",index = False)
print("***raw2 part 8 Saved***")

#Third one
raw3 = raw3(Return,KalaAnbar)
raw3[0].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Return.csv",encoding = "utf-8-sig")
print("***raw3 part 0 Saved***")
raw3[1].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\ReturnDetail.csv",encoding = "utf-8-sig")
print("***raw3 part 1 Saved***")

#Fifth one
raw4 = raw4(AghlamTasvie,Chek,DateTable)
raw4[0].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Cheque.csv",encoding = "utf-8-sig")
print("***raw4 part 0 Saved***")
raw4[1].to_csv(r"D:\AlizadeAdel\Reporting System\data_input\structured\Adjustment.csv",encoding = "utf-8-sig")
print("***raw4 part 1 Saved***")

print("***Your  Data of Structured Reports Is Ready to Use***")

