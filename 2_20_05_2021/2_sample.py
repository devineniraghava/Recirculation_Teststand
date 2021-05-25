# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:33:55 2021

@author: Devineni
"""
import pandas as pd
import matplotlib.pyplot as plt

pd.options.plotting.backend = "matplotlib"

import os
sensor_list = ['1c', '3b', '2L', '2e', 'außen', '1T', '2a_50', '2c_50', '2d', '4T', '3h', 
     '3L_Kü', '2T', '4L', '3d', '1L', '3a_50']
pos = pd.read_excel("C:/Users/Devineni/OneDrive - bwedu/6_Recirculation_Teststand/2_20_05_2021/sensor_positions.xlsx")

#%% get absolute path for the files 

location = "C:/Users/Devineni/OneDrive - bwedu/6_Recirculation_Teststand/2_20_05_2021/excel data/"

abs_path = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(location):
   for item in f:
      if '.xlsx' in item:
         abs_path.append(os.path.join(r, item))
#%%
# fig , ax = plt.subplots()

df_list = []

for file in abs_path:
        
    df1 = pd.read_excel(file, skiprows = 1)
    df1 = df1.iloc[:,[1,4]]
    name = [sensor for sensor in sensor_list if sensor in file]
    legends = pos.loc[pos["sensor"] == name[0],["legend"]].iat[0,0]
    df1.columns = ["datetime", legends]

    print(df1.dtypes)

    df1 = df1.set_index("datetime")
    # df1.plot(y = legends, ax = ax)
    df_list.append(df1)
#%%

co2_df = pd.concat(df_list, axis = 1).fillna(0)
co2_df = co2_df=co2_df.astype("int")
co2_df.to_excel("save1.xlsx")
# co2_df = co2_df.iloc[:,[0,9,10,12]]
#%%
pd.options.plotting.backend = "plotly"

import plotly.express as px

# df = px.data.stocks()
df = pd.read_excel("save1.xlsx")
df = df[sorted(df.columns)]

fig = px.line(df, x="datetime", y=df.columns, title='60 m3/hr (Thursday), 1) Entire AC closed loop and 2) Test stand closed loop')

fig.show()


import plotly.io as pio

pio.renderers.default='browser'



#%%










#%%



















