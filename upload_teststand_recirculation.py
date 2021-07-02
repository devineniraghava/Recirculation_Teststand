# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:25:02 2021

@author: Raghavakrishna
"""

# Packages

import pandas as pd
from openpyxl import load_workbook
def prRed(skk): print("\033[31;1;m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[33;1;m {}\033[00m" .format(skk)) 
import os
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:Password123@localhost/teststand_recirculation",pool_pre_ping=True)

#%%
# =============================================================================
# location = "C:/Users/Raghavakrishna/OneDrive - bwedu/6_Recirculation_Teststand"
# 
# abs_path = []
# 
# # r=>root, d=>directories, f=>files
# for r, d, f in os.walk(location):
#     for item in f:
#       if 'save' in item:
#           abs_path.append(os.path.join(r, item))
# #%%
# df_list = []
# 
# for path in abs_path:
#     a1 = pd.read_excel(path)
#     df_list.append(a1)
#     prYellow(path)
#     
# #%%
# 
# test_stand_data = pd.concat(df_list,axis = 0).fillna(0)
# 
# test_stand_data = test_stand_data.set_index("datetime")
# #%%
# test_stand_data.to_sql("recirculation", con = engine , if_exists="replace")
# 
# test_stand_data.to_sql("recirculation", con = create_engine("mysql+pymysql://wojtek:Password#102@wojtek.mysql.database.azure.com/teststand_recirculation",pool_pre_ping=True), if_exists="replace")
# 
# =============================================================================
#%%


# df = pd.read_csv("remus/skt_20210623.csv", sep=',',  index_col=False, dtype='unicode', parse_dates = {"datetime":[0,1]})




#%%
# =============================================================================
# test_stand_data = pd.read_sql_query("SELECT * FROM teststand_recirculation.recirculation;", con = engine)
# 
# 
# 
# 
# 
# #%%
# pd.options.plotting.backend = "plotly"
# 
# import plotly.io as pio
# pio.renderers.default='browser'
# 
# import plotly.express as px
# 
# 
# fig = px.line(test_stand_data, x="datetime", y=test_stand_data.columns, title='Outdoor: 20°C , 60 %RH  Indoor: 2°C, 34 %RH1) 60 m3/hr , and 2) 80 m3/hr')
# fig.show()
# 
# 
# import plotly.io as pio
# pio.renderers.default='browser'
# 
# 
# pd.options.plotting.backend = "matplotlib"
# =============================================================================

#%%

# a = df.copy()



# a[a.columns[1:]] = a.iloc[:,1:].astype("float")

# print(a.dtypes)

# a.to_csv("remus/skt_20210623_clean.csv", index = False)

#%%

location = "C:/Users/Raghavakrishna/OneDrive - bwedu/6_Recirculation_Teststand/remus"

abs_path = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(location):
    for item in f:
      if 'clean' in item:
          abs_path.append(os.path.join(r, item))

#%%

df_list = []
for path in abs_path:
    df = pd.read_csv(path)
    df_list.append(df)
    print(path)


mega_df = pd.concat(df_list)
mega_df["datetime"] = pd.to_datetime(mega_df["datetime"], format = "%Y-%m-%d %H:%M:%S")

#%%




mega_df.to_sql("remus", con = engine, chunksize = 10000, if_exists="replace", index = False)

#%%





















