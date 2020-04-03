

import os
import pandas as pd
import numpy as np

Year = int(input("Year : "))
Month = int(input("Month : "))

#In Path taghir konad
files = os.listdir(r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\services\BI dashboards\بهمن 98\R3-SalesAndReturn-2020-Feb\GoalFiles\Goals_For_Code")
df_total = pd.DataFrame({"SC0" : 1,
                         "DealerID" : 1,
                         "هدف" : 1,
                         "DateID" : 1,
                        "salesType": 1},index = [1])
df_total.drop(index = 1,inplace = True)
Cols = []



for i in files :
    print(i)
    #In path Taghir konad
    path = r'C:\Users\a.alizadeh\Desktop\علیزاده عادل\services\BI dashboards\بهمن 98\R3-SalesAndReturn-2020-Feb\GoalFiles\Goals_For_Code\{}'.format(i)
    df0 = pd.read_excel(path,sheet_name = "Sheet2")
    constants = list(df0.columns)

    df = pd.read_excel(path).fillna(0)

    Cols = list(df.columns)[1:]
    for i in Cols :
        print(str(i) + ": " + str(type(i)))
    for i in Cols:
        if i == "143033.1" or i == "121013.1" or i == "153031.1":
            Cols.remove(i)
            Cols.append(int(i[:6]))
    
    df = pd.melt(df,id_vars = ['x'],value_vars = Cols)
    #In path taghir konad
    Date = pd.read_excel(r".xlsx")
    working_days = Date[Date["Key"] == 1].count()[1]
    Date = Date[(Date["Key"] == 1) & (Date["Month"] == Month) & (Date["Year"] == Year) ]
    df['value'] = df['value']/working_days
    df.rename(columns = {'x' : 'SC0','variable' : 'کد ویزیتور', 'value' : 'هدف'},inplace = True)
    df = df[df['هدف'] != 0]
    df.reset_index(drop = True,inplace = True)
      
      
    Date["k"] = 0
    df["k"] = 0
    df["salesType"] = constants[1]
    df["Line"] = constants[0]
    df["کد ویزیتور"] = df["کد ویزیتور"].astype("str")
    
    df_count = df.count()[1]
    df["DealerID"] = df["کد ویزیتور"] + pd.Series(["-"]*df_count) + df["Line"]

    df1 = pd.merge(df,Date,on = "k")
    
    df1 = df1[["SC0","هدف","DealerID","DateID","salesType"]]
    df_total = df_total.append(df1)
#In path taghir konad
df_total.to_excel(r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\services\BI dashboards\بهمن 98\R3-SalesAndReturn-2020-Feb\GoalFiles\Goals-From-Code.xlsx",index = False)
print("Done")





