# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


#Paths
#KalaForosh = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Kala-Forosh98.xlsx"
#KalaAnbar = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Kala-Anbar98.xlsx"
#GoalsCategory = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\LookupTables\GoalsCategory.xlsx"
    
def raw1(KalaForosh,KalaAnbar,GoalsCategory) :
    print("***raw1 executed***")
    #Product ProductCategories
    df0 = pd.read_excel(KalaForosh,usecols = ["تولید کننده","نام تجاری","گروه کالا","کد کالا","نام کالا"])
    print("***raw1 df0 obtaiend***")
    df1 = pd.read_excel(GoalsCategory)
    print("***raw1 df1 obtaiend***")
    df2 = pd.read_excel(KalaAnbar,usecols = ["کد کالا","تعداد در کارتن"])
    print("***raw1 df2 obtaiend***")
    df3 = pd.merge(df0,df1,how = "left", on = "کد کالا")
    df3 = pd.merge(df3,df2,how = "left", on = "کد کالا")
    ProductCategories = df3[["گروه کالا","نام تجاری","تولید کننده","GoalsCategory"]]
    ProductCategories.drop_duplicates(subset = None,keep = "first",inplace = True)
    Product = df3[["کد کالا","نام کالا","GoalsCategory","تعداد در کارتن"]]
    print("***raw1 finished***")
    return Product,ProductCategories



  