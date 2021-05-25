# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:45:59 2021

@author: Devineni
"""
from tabulate import tabulate
import pandas as pd
pd.options.plotting.backend = "matplotlib"

import os
import matplotlib.pyplot as plt

sensor_list = ['1c', '3b', '2L', '2e', 'außen', '1T', '2a_50', '2c_50', '2d', '4T', '3h', 
     '3L_Kü', '2T', '4L', '3d', '1L', '3a_50']
pos = pd.read_excel("C:/Users/Devineni/OneDrive - bwedu/6_Recirculation_Teststand/2_20_05_2021/sensor_positions.xlsx")

#%% get absolute path of all .xlsx files

location = "C:/Users/Devineni/OneDrive - bwedu/6_Recirculation_Teststand/1_19_05_2021/"

files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(location):
   for item in f:
      if '.xlsx' in item:
         files_in_dir.append(os.path.join(r, item))

# for item in files_in_dir:
#    print("file in dir: ", item)
            

#%%
fig , ax = plt.subplots()
df_list = []


for file in files_in_dir:
        
    df1 = pd.read_excel(file, skiprows = 1)
    df1 = df1.iloc[:,[1,4]]
    name = [sensor for sensor in sensor_list if sensor in file]
    legends = pos.loc[pos["sensor"] == name[0],["legend"]].iat[0,0]
    df1.columns = ["datetime", name[0]]
    df1 = df1.set_index("datetime")
    df1.plot(y = name[0], ax = ax, label = name[0])
    df_list.append(df1)
    
#%%

co2_df = pd.concat(df_list, axis = 1).fillna(0)
co2_df = co2_df=co2_df.astype("int")
co2_df = co2_df[sorted(co2_df.columns)]


#%%
pd.options.plotting.backend = "plotly"




import plotly.express as px

# df = px.data.stocks()
df = co2_df.copy().reset_index()
fig = px.line(df, x="datetime", y=df.columns, title="Last Wednesday")
fig.add_annotation(x="2021-05-19 17:08:00", y=100,
            text="Text annotation with arrow",
            showarrow=False,
            yshift=10)


fig.show()


import plotly.io as pio

pio.renderers.default='browser'





#%%
	










#%%