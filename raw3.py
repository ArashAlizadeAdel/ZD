# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#Paths
#Return = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Aghlam-Bargasht-Az-Forosh98.xlsx"
#KalaAnbar = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Kala-Anbar98.xlsx"

def raw3(Return,KalaAnbar):
    print("***raw3 executed***")
    #Getting raw data
    df0 = pd.read_excel(Return,usecols = ["فروشنده","تعداد برگشتی و جایزه برگشتی-ظرف","مبلغ برگشتی خالص","شماره سند انبار","علت برگشت","کد کالا","کد فروشنده","کد مشتری","دفتر فروش","شماره فاکتور عطف","تاریخ برگشت فاکتور","شماره برگشت فاکتور"])
    print("***raw3 df0 obtaiend***")
    df1 = pd.read_excel(KalaAnbar)
    print("***raw3 df1 obtaiend***")
    
    
    #Preparing data for furthur analysis
    df0 = df0.fillna(0)
    df0 = df0.astype({"شماره برگشت فاکتور" : np.int , "شماره فاکتور عطف" : np.int , "کد فروشنده" : np.int , "کد مشتری" : np.int})
    df0 = df0.astype({"شماره برگشت فاکتور" : np.str , "شماره فاکتور عطف" : np.str , "کد فروشنده" : np.str , "کد مشتری" : np.str})
    df0["ReturnID"] = df0["شماره برگشت فاکتور"] + df0["کد فروشنده"] + df0["دفتر فروش"]
    df0["DealerID"] = df0["کد فروشنده"] + "-" + df0["دفتر فروش"]
    df0["SaleType"] = np.where(df0["فروشنده"].str.contains("حمل ", regex = False),"حمل مستقیم","خرده فروشی")
    df1 = df1[["کد کالا","تعداد در کارتن"]]
    df0 = pd.merge(df0,df1,how = "left",on = "کد کالا")
    
    
    #Return
    Return = df0[["شماره برگشت فاکتور","شماره فاکتور عطف","DealerID","SaleType","ReturnID","کد مشتری","تاریخ برگشت فاکتور","علت برگشت","شماره سند انبار",]].drop_duplicates(subset = None,keep = "first",inplace = False)
    
    
    #ReturnDetail
    ReturnDetail = df0[["ReturnID","کد کالا","تعداد در کارتن","تعداد برگشتی و جایزه برگشتی-ظرف","مبلغ برگشتی خالص","DealerID","SaleType"]]
    ReturnDetail["کارتن برگشتی"] = ReturnDetail["تعداد برگشتی و جایزه برگشتی-ظرف"]/ReturnDetail["تعداد در کارتن"]
    ReturnDetail = ReturnDetail[["ReturnID","مبلغ برگشتی خالص","کارتن برگشتی","کد کالا","DealerID","SaleType"]]
    print("***raw3 finished***")
    return Return,ReturnDetail
