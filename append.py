#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[3]:


files = os.listdir(r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\اقلام گردش فروش")


# In[4]:


Cols = ["کد مشتری","نام مشتری","نام فروشگاه","طبقه","فعالیت","استان","شهر","کد فروشنده","فروشنده","مامور توزیع کرده","نام مرکز","دفتر فروش","شماره توزیع","تاریخ توزیع","شماره خروجی","تاریخ خروجی","شماره درخواست","تاریخ درخواست","شماره حواله","تاریخ حواله","شماره فاکتور","تاریخ فاکتور","نام گروه","کد کالا","نام کالا","تعداد حواله - ظرف","تعداد جايزه حواله - ظرف","مبلغ ناخالص حواله","مبلغ کل تخفیف حواله","مبلغ خالص حواله","علت مرجوعی","تعداد مرجوعي - ظرف","تعداد جايزه مرجوعي - ظرف","مبلغ ناخالص مرجوعی","مبلغ کل تخفیف مرجوعی","مبلغ خالص مرجوعی","تعداد فاكتور- ظرف","تعداد جايزه فاكتور - ظرف","مبلغ ناخالص فاکتور","مبلغ کل تخفیف فاکتور","مبلغ خالص فاکتور","مبلغ ناخالص فاكتور با کسر برگشتی","نوع درخواست","مبلغ كل تخفيف فاكتور با کسر برگشتی"]
Dictfortotal = {}
for i in Cols:
    Dictfortotal[i] = 1

df_total = pd.DataFrame(Dictfortotal,index = [1])
df_total.drop(index = 1,inplace = True)
df_total


# In[5]:


for i in files:
    path = r'C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\اقلام گردش فروش\{}'.format(i)
    df0 = pd.read_excel(path,usecols = Cols )
    df_total = df_total.append(df0)
    print(i)
print("Going to make the result")
print("Done!")


# In[6]:


df_total
df_total.to_csv(r"C:\Users\a.alizadeh\Desktop\علیزاده عادل\DataCenter\98\Aghlam-Gardesh98.csv",chunksize = 2000)


# In[ ]:




