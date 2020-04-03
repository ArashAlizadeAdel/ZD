# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import datetime as dt

#Paths
#SaleTurnOver = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\اقلام گردش فروش\2020-02.xlsx"
#Invoice_Acc = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Factor-TarikhFactor-HesabDari98.xlsx"
#Invoice_Sale = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Factor-TarikhFactor-Forosh98.xlsx"
#KalaAnbar = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Kala-Anbar98.xlsx"
#DateTable = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\DateTable.xlsx"
#Moshtari = r"D:\AlizadeAdel\Reporting System\data_raw\structured\Moshtari98.xlsx"


def raw2(SaleTurnOver,Invoice_Acc,Invoice_Sale,KalaAnbar,DateTable,Moshtari):
    print("***raw2 executed***")
    LastUpdate = dt.datetime.utcfromtimestamp(os.path.getmtime(SaleTurnOver))
    
    #Getting raw data
    df0 = pd.read_excel(SaleTurnOver,usecols = ["مبلغ خالص فاکتور","تعداد جايزه فاكتور - ظرف","تعداد فاكتور- ظرف","مبلغ خالص مرجوعی","تعداد جايزه مرجوعي - ظرف","تعداد مرجوعي - ظرف","علت مرجوعی","مبلغ خالص حواله","کد کالا","تاریخ فاکتور","شماره فاکتور","تاریخ حواله","شماره حواله","نوع درخواست","تاریخ درخواست","شماره درخواست","شماره توزیع","تاریخ خروجی","شماره خروجی","دفتر فروش","نام مرکز","مامور توزیع کرده","کد فروشنده","شهر","فروشنده","کد مشتری","تعداد جايزه حواله - ظرف","تعداد حواله - ظرف"])
    print("***raw2 df0 obtaiend***")
    df1 = pd.read_excel(Invoice_Sale,usecols = ["نام مرکز","دفتر فروش","فروشنده","کد فروشنده","مامور توزیع کرده","کد مشتری","نام فروشگاه","شماره حواله","شماره فاکتور","شماره توزیع"])
    print("***raw2 df1 obtaiend***")
    df2 = pd.read_excel(Invoice_Acc,usecols = ["مرکز توزیع","دفتر فروش","کد فروشنده","مامور توزیع کرده","کد مشتری","نام فروشگاه","نوع فعالیت","مانده فاکتور","شماره حواله","شماره فاکتور","شماره توزیع","تاریخ فاکتور","نام فروشنده"])
    print("***raw2 df2 obtaiend***")
    df3 = pd.read_excel(KalaAnbar)
    print("***raw2 df3 obtaiend***")
    df4 = pd.read_excel(DateTable)
    print("***raw2 df4 obtaiend***")
    df5 = pd.read_excel(Moshtari,usecols =["کد مشتری","نام فروشگاه","فعالیت مشتری","شهر"])
    print("***raw2 df5 obtaiend***")
    
    
    #Preparing data for furthur analysis
    df0 = df0.fillna(0)
    df1 = df1.fillna(0)
    df2 = df2.fillna(0)
    df0 = df0.astype({ "شماره حواله": np.int , "شماره فاکتور": np.int , "شماره توزیع" : np.int, "کد فروشنده" : np.int , "کد مشتری" : np.int,"شماره خروجی" : np.int})
    df0 = df0.astype({ "شماره حواله": np.str , "شماره فاکتور": np.str , "شماره توزیع" : np.str, "کد فروشنده" : np.str , "کد مشتری" : np.str, "مامور توزیع کرده" : np.str,"شماره خروجی" : np.str, "تاریخ فاکتور" : np.str})
    df1 = df1.astype({ "شماره حواله": np.int , "شماره فاکتور": np.int , "شماره توزیع" : np.int, "کد فروشنده" : np.int , "کد مشتری" : np.int})
    df1 = df1.astype({ "شماره حواله": np.str , "شماره فاکتور": np.str , "شماره توزیع" : np.str, "کد فروشنده" : np.str , "کد مشتری" : np.str})
    df2 = df2.astype({ "شماره حواله": np.int , "شماره فاکتور": np.int , "شماره توزیع" : np.int, "کد فروشنده" : np.int , "کد مشتری" : np.int})
    df2 = df2.astype({ "شماره حواله": np.str , "شماره فاکتور": np.str , "شماره توزیع" : np.str, "کد فروشنده" : np.str , "کد مشتری" : np.str,"تاریخ فاکتور" : np.str})
    df0["InvoiceID"] = df0["کد فروشنده"] + df0["کد مشتری"] + df0["شماره حواله"] + df0["شماره فاکتور"]
    df0["InvoiceIDFinance"] = df0["کد فروشنده"] + df0["کد مشتری"] + df0["تاریخ فاکتور"] + df0["شماره فاکتور"]
    df1["InvoiceID"] = df1["کد فروشنده"] + df1["کد مشتری"] + df1["شماره حواله"] + df1["شماره فاکتور"]
    df2["InvoiceID"] = df2["کد فروشنده"] + df2["کد مشتری"] + df2["شماره حواله"] + df2["شماره فاکتور"]
    df2["InvoiceIDFinance"] = df2["کد فروشنده"] + df2["کد مشتری"] + df2["تاریخ فاکتور"] + df2["شماره فاکتور"]
    df3 = df3[["کد کالا","تعداد در کارتن"]]
    
    #Dealer 
    Dealer = df1[["کد فروشنده","فروشنده","نام مرکز","دفتر فروش"]].drop_duplicates(subset = None,keep = "first",inplace = False)
    Dealer["DealerID"] = Dealer["کد فروشنده"] + "-" + Dealer["دفتر فروش"]
    Dealer["LineID"] = Dealer["نام مرکز"] + "-" + Dealer["دفتر فروش"]
    Dealer = Dealer[["DealerID","LineID","کد فروشنده","فروشنده"]]
    
    
    #Distributer
    Dister = df1[["دفتر فروش","نام مرکز","مامور توزیع کرده"]].drop_duplicates(subset = None,keep = "first",inplace = False)
    Dister = Dister[Dister["مامور توزیع کرده"] != 0]
    Dister["DisterID"] = Dister["مامور توزیع کرده"] + "-" + Dister["دفتر فروش"]
    Dister["LineID"] = Dister["نام مرکز"] + "-" + Dister["دفتر فروش"]
    Dister = Dister[["DisterID","LineID","مامور توزیع کرده"]]
    Dister = Dister.dropna(subset = ["مامور توزیع کرده"])
    
    
    #Customer
    Customer = df5
    
    #ReturnCause
    
    ReturnCause = df0[["علت مرجوعی"]].drop_duplicates(subset = None,keep = "first",inplace = False)
    ReturnCause = ReturnCause.dropna()
    
    #DistributionCenter & Line
    DistCenter_Line = df0[["نام مرکز","دفتر فروش"]].drop_duplicates(subset = None,keep = "first",inplace = False)
    DistCenter_Line["LineID"] = DistCenter_Line["نام مرکز"] + "-" + DistCenter_Line["دفتر فروش"]
    
    
    #Invoice
    Invoice = df0[["فروشنده","علت مرجوعی","تاریخ فاکتور","شماره فاکتور","InvoiceID","InvoiceIDFinance","تاریخ حواله","دفتر فروش","شماره حواله","نوع درخواست","تاریخ درخواست","شماره درخواست","شماره توزیع","تاریخ خروجی","شماره خروجی","مامور توزیع کرده","کد فروشنده","شهر","کد مشتری"]]
    Invoice["DealerID"] = Invoice["کد فروشنده"] + "-" + Invoice["دفتر فروش"]
    Invoice["DisterID"] = Invoice["مامور توزیع کرده"] + "-" + Invoice["دفتر فروش"]
    Invoice["DateID"] = np.where(Invoice["تاریخ فاکتور"] == "0",Invoice["تاریخ حواله"],Invoice["تاریخ فاکتور"])
    Invoice = Invoice[["علت مرجوعی","تاریخ فاکتور","شماره فاکتور","تاریخ حواله","شماره حواله","نوع درخواست","تاریخ درخواست","شماره درخواست","شماره توزیع","تاریخ خروجی","شماره خروجی","فروشنده","شهر","کد مشتری","DisterID","DealerID","InvoiceID","InvoiceIDFinance","DateID"]]
    Invoice = Invoice.drop_duplicates(subset = None,keep = "first",inplace = False)
    Invoice["SaleType"] = np.where(Invoice["فروشنده"].str.contains("حمل ", regex = False),"حمل مستقیم","خرده فروشی")
    #creating ReturnAmount and NetSaleAmount for furthur analysis
    ReturnAmount = df0[["InvoiceID","مبلغ خالص مرجوعی","مبلغ خالص فاکتور"]]
    ReturnAmount = ReturnAmount.groupby(["InvoiceID"]).sum()
    Invoice = pd.merge(Invoice,ReturnAmount,how = "left", on = "InvoiceID")
    #Invoice -- InvoiceStatus Column Development
    Invoice["RequestFeature"] = np.where(Invoice["شماره حواله"] == "0","WithoutHavale","WithHavale")
    #Y before texts are for furthur checkings
    Invoice["DistStatus"] = np.where(Invoice["RequestFeature"] == "WithHavale" ,
           np.where(Invoice["شماره خروجی"] == "0" , "NotDistributed" , "YDistributed"),
           np.where(Invoice["شماره خروجی"] == "0" , "NotDistributedWithoutHavale" , "YDistributedWithoutHavale"))
    Invoice["DistFeature"] = np.where(Invoice["DistStatus"].str.contains("Y", regex = False),
           np.where(Invoice["شماره فاکتور"] == "0" , "NotFactored" , "YFactored"),
           "NotDistributed")
    Invoice["NotFactoredFeature"] = np.where(Invoice["DistFeature"] == "NotFactored" ,
       np.where(Invoice["نوع درخواست"].str.contains("FOC", regex = False),"FOC",
                np.where(Invoice["مبلغ خالص مرجوعی"] > 0,"کل مرجوع","بلاتکلیف")),
       "YFactored")
    Invoice["FactoredFeature"] = np.where(Invoice["NotFactoredFeature"] == "YFactored" ,
       np.where(Invoice["نوع درخواست"].str.contains("FOC", regex = False),"FOC",
                np.where(Invoice["مبلغ خالص فاکتور"] == 0,"تخفیف صد در صد",
                         np.where(Invoice["مبلغ خالص مرجوعی"] > 0, "جز مرجوع","بدون مرجوعی" ))),
       "NotFactored")
    Invoice["InvoiceStatus"] = np.where(Invoice["DistStatus"] == "NotDistributed" ,"توزیع نشده" ,
           np.where(Invoice["DistStatus"] == "NotDistributedWithoutHavale" ,"توزیع نشده - بدون حواله" ,
                    np.where(Invoice["NotFactoredFeature"] == "YFactored" ,Invoice["FactoredFeature"] ,
                             np.where(Invoice["FactoredFeature"] == "NotFactored" ,Invoice["NotFactoredFeature"] ,"Error"))))
    Invoice = Invoice[["InvoiceStatus","FactoredFeature","NotFactoredFeature","DistFeature","DistStatus","RequestFeature","SaleType","InvoiceID","InvoiceIDFinance","DealerID","DisterID","کد مشتری","شهر","شماره خروجی","تاریخ خروجی","شماره توزیع","شماره درخواست","تاریخ درخواست","نوع درخواست","شماره حواله","تاریخ حواله","شماره فاکتور","تاریخ فاکتور","علت مرجوعی","DateID","مبلغ خالص فاکتور"]]
    Invoice["LastUpdate"] = LastUpdate
    
    
    
    #InvoiceDetail
    InvoiceDetail = pd.merge(df0,df3,how = "left",on = "کد کالا")
    InvoiceDetail = InvoiceDetail.fillna(value = {"تعداد در کارتن" : 24})
    InvoiceDetail["خالص روکش"] = np.where(InvoiceDetail["مبلغ خالص حواله"] == 0 ,InvoiceDetail["مبلغ خالص فاکتور"] ,InvoiceDetail["مبلغ خالص حواله"] )
    InvoiceDetail["ZarfMarjoiee"] = InvoiceDetail["تعداد مرجوعي - ظرف"] + InvoiceDetail["تعداد جايزه مرجوعي - ظرف"]
    InvoiceDetail["ZarfRokesh"] = np.where(InvoiceDetail["مبلغ خالص حواله"] == 0 ,InvoiceDetail["تعداد فاكتور- ظرف"] + InvoiceDetail["تعداد جايزه فاكتور - ظرف"] ,InvoiceDetail["تعداد حواله - ظرف"] + InvoiceDetail["تعداد جايزه حواله - ظرف"] )
    InvoiceDetail["کارتن مرجوعی"] = InvoiceDetail["ZarfMarjoiee"]/InvoiceDetail["تعداد در کارتن"]
    InvoiceDetail["کارتن روکش"] = InvoiceDetail["ZarfRokesh"]/InvoiceDetail["تعداد در کارتن"]
    InvoiceDetail = InvoiceDetail[["InvoiceID","InvoiceIDFinance","خالص روکش","کارتن مرجوعی","کارتن روکش","مبلغ خالص مرجوعی"]]
    
    #InvoiceAll -- this is for ModatZamanVosol
    
    InvoiceAll = df2
    InvoiceAll["DealerID"] = InvoiceAll["کد فروشنده"] + "-" + InvoiceAll["دفتر فروش"]
    InvoiceAll["SaleType"] = np.where(InvoiceAll["نام فروشنده"].str.contains("حمل ", regex = False),"حمل مستقیم","خرده فروشی")
    InvoiceAll = InvoiceAll[["کد مشتری","مانده فاکتور","شماره حواله","شماره فاکتور","شماره توزیع","تاریخ فاکتور","SaleType","DealerID","InvoiceID","InvoiceIDFinance"]]
    
    #Debt
    Debt = InvoiceAll[InvoiceAll["مانده فاکتور"] > 0]
    
    df4["InvoiceDate"] = df4["Date"]
    Debt = pd.merge(Debt,df4[["Sdate","InvoiceDate"]],how = "left", left_on = "تاریخ فاکتور", right_on = "Sdate").drop(columns = ["Sdate"])
    Debt["NOW"] = pd.Timestamp.now()
    df6 = pd.DataFrame({"DayAhead" : [0,5,10,15,20,25,30,35,40,45,50]})
    Debt["CommonKey"] = 0
    df6["CommonKey"] = 0
    Debt = Debt.merge(df6,on = "CommonKey")
    Debt = Debt[["InvoiceIDFinance","مانده فاکتور","InvoiceDate","NOW","DayAhead"]]
    Debt["HypAdjustmentTime"] = Debt["NOW"] + pd.to_timedelta(Debt["DayAhead"], unit='d')
    Debt["HypAdjustmentTimeSpan"] = ((Debt["HypAdjustmentTime"] - Debt["InvoiceDate"]))/np.timedelta64(1, 'D')
    Debt["WeightedAVGNumerator"] = Debt["HypAdjustmentTimeSpan"] * Debt["مانده فاکتور"]
    Debt = Debt[["InvoiceIDFinance","DayAhead","InvoiceDate","HypAdjustmentTime","WeightedAVGNumerator"]]
    print("***raw2 finished***")
    return Dealer,Dister,Customer,ReturnCause,DistCenter_Line,Invoice,InvoiceDetail,Debt,InvoiceAll
    

