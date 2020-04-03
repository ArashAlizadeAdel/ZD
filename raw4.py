# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


#Paths
AghlamTasvie = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Aghlam-Tasvie98.xlsx"
Chek = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Chek98.xlsx"
DateTable = r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\DateTable.xlsx"

def raw4(AghlamTasvie,Chek,DateTable):
    print("***raw4 executed***")
    #Getting raw data
    df0 = pd.read_excel(Chek,usecols = ["شماره چک","تاریخ چک","کد مشتری","کد فروشنده","آخرین وضعیت","تاریخ آخرین وضعیت","تاریخ برگشت"])
    print("***raw4 df0 obtaiend***")
    df1 = pd.read_excel(AghlamTasvie,usecols = ["نوع پرداخت","شماره سند","تاریخ سند","تاریخ حواله","مبلغ سند","کد مشتری","تاریخ چک","شماره حواله","شماره فاکتور","شماره چک","کد فروشنده","تاریخ فاکتور"])
    print("***raw4 df1 obtaiend***")
    df2 = pd.read_excel(DateTable)
    print("***raw4 df2 obtaiend***")
    
    
    #Preparing data for furthur analysis
    df0 = df0.fillna(0)
    df1 = df1.fillna(0)
    df0 = df0.replace(["454731/53","45473016/16"],[45473153,4547301616])
    df1 = df1.replace(["454731/53","45473016/16"],[45473153,4547301616])
    df0 = df0.astype({"کد فروشنده" : np.int , "کد مشتری" : np.int, "شماره چک" : np.int64})
    df0 = df0.astype({"کد فروشنده" : np.str , "کد مشتری" : np.str,"شماره چک" : np.str,"تاریخ برگشت" : np.str})
    df1 = df1.astype({ "شماره فاکتور": np.int, "کد فروشنده" : np.int , "کد مشتری" : np.int,"شماره چک" : np.int64})
    df1 = df1.astype({ "شماره فاکتور": np.str, "کد فروشنده" : np.str , "کد مشتری" : np.str,"شماره چک" : np.str,"تاریخ چک" : np.str})
    df0["ChequeID"] = df0["شماره چک"] + df0["تاریخ چک"] + df0["کد مشتری"]
    df1["ChequeID"] = df1["شماره چک"] + df1["تاریخ چک"] + df1["کد مشتری"]
    df1["InvoiceIDFinance"] = df1["کد فروشنده"] + df1["کد مشتری"] + df1["تاریخ فاکتور"] + df1["شماره فاکتور"]
    df1["ChequeID"] = df1["شماره چک"] + df1["تاریخ چک"] + df1["کد مشتری"]
    
    
    #Cheque
    Cheque = df0
    
    
    #Adjustment
    #Merging Adjustment with Cheque for furthur analysis
    Adjustment = pd.merge(df1,Cheque[["ChequeID","آخرین وضعیت","تاریخ آخرین وضعیت","تاریخ برگشت"]],how = "left", on = "ChequeID")
    #Converting dates, because we need names that are understandable and we need Miladi Date
    df2["ChequeDate"] = df2["Date"]
    df2["InvoiceDate"] = df2["Date"]
    df2["HavaleDate"] = df2["Date"]
    df2["SanadDate"] = df2["Date"]
    df2["LastStatusDate"] = df2["Date"]
    Adjustment = pd.merge(Adjustment,df2[["Sdate","ChequeDate"]],how = "left", left_on = "تاریخ چک", right_on = "Sdate").drop(columns = ["Sdate"])
    Adjustment = pd.merge(Adjustment,df2[["Sdate","InvoiceDate"]],how = "left", left_on = "تاریخ فاکتور", right_on = "Sdate").drop(columns = ["Sdate"])
    Adjustment = pd.merge(Adjustment,df2[["Sdate","HavaleDate"]],how = "left", left_on = "تاریخ حواله", right_on = "Sdate").drop(columns = ["Sdate"])
    Adjustment = pd.merge(Adjustment,df2[["Sdate","SanadDate"]],how = "left", left_on = "تاریخ سند", right_on = "Sdate").drop(columns = ["Sdate"])
    Adjustment = pd.merge(Adjustment,df2[["Sdate","LastStatusDate"]],how = "left", left_on = "تاریخ آخرین وضعیت", right_on = "Sdate").drop(columns = ["Sdate"])
    Adjustment["ChequeTimeSpan"] = (Adjustment["ChequeDate"] - Adjustment["InvoiceDate"])/np.timedelta64(1, 'D')
    Adjustment = Adjustment.astype({"ChequeTimeSpan" : np.float})
    
    Adjustment["Category"] = np.where(Adjustment["شماره حواله"] != 0, "حواله",
                                  np.where(Adjustment["نوع پرداخت"] != "چك" , "نقد و سایر" ,
                                           np.where(Adjustment["ChequeTimeSpan"] >= 30 ,"چک سی روز به بالا" ,
                                                    np.where(Adjustment["ChequeTimeSpan"] >= 20 ,"چک بیست تا 29 روز" ,
                                                             np.where(Adjustment["ChequeTimeSpan"] >= 10 ,"چک ده تا 19 روز" ,
                                                                      np.where(Adjustment["ChequeTimeSpan"] >= 5 ,"چک پنج تا 9 روز" ,
                                                                               np.where(Adjustment["ChequeTimeSpan"] >= 0 ,"چک زیر پنج روز" ,"چک با روز نامعتبر")))))))
    
    
    
    Adjustment["ToBeCountedOrNot"] = np.where(((Adjustment["آخرین وضعیت"] == "برگشتي") | (Adjustment["آخرین وضعیت"] =="استرداد" )) ,1, 0 )
    Adjustment["تاریخ برگشت"] = np.where(Adjustment["تاریخ برگشت"].isna(),"0",Adjustment["تاریخ برگشت"])
    Adjustment["AdjustmentDoneDateIndex"] = np.where(Adjustment["نوع پرداخت"] == "واريز", 1,
              np.where(Adjustment["نوع پرداخت"] =="چك",np.where(Adjustment["تاریخ برگشت"] == "0" ,2,3),
                       4))
    Adjustment["AdjustmentDate"] = np.where(Adjustment["AdjustmentDoneDateIndex"] ==1 , Adjustment["HavaleDate"],
              np.where(Adjustment["AdjustmentDoneDateIndex"] ==2,Adjustment["ChequeDate"] + pd.DateOffset(days=1),
                       np.where(Adjustment["AdjustmentDoneDateIndex"] ==3,Adjustment["LastStatusDate"],
                                Adjustment["SanadDate"])))
    Adjustment["AdjustmentTimeSpan"] = ((Adjustment["AdjustmentDate"] - Adjustment["InvoiceDate"]))/np.timedelta64(1, 'D')
    Adjustment["AdjustmentTimeSpan"] = np.where(Adjustment["AdjustmentTimeSpan"] < 0 , 0 , Adjustment["AdjustmentTimeSpan"])
    Adjustment["WeightedAVGNumerator"] = Adjustment["AdjustmentTimeSpan"] * Adjustment["مبلغ سند"]
    Adjustment = Adjustment[["InvoiceIDFinance","ChequeID","نوع پرداخت","Category","InvoiceDate","AdjustmentDate","WeightedAVGNumerator"]]
    print("***raw4 finished***")
    return Cheque,Adjustment

