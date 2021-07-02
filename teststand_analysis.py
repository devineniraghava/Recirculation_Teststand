# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 07:42:31 2021

@author: Raghavakrishna
"""

# Packages

import pandas as pd
from easygui import *

def prRed(skk): print("\033[31;1;m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[33;1;m {}\033[00m" .format(skk)) 
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:Password123@localhost/teststand_recirculation",pool_pre_ping=True)
azure = create_engine("mysql+pymysql://wojtek:Password#102@wojtek.mysql.database.azure.com/teststand_recirculation",pool_pre_ping=True)

#%%

times = pd.read_sql_query("SELECT * FROM teststand_recirculation.times;", con = engine).drop("times_id", axis = 1)
# msgbox(times, ok_button="Good job!")


class TestStand:
    
    def __init__(self, value = 0):
        self.value = value
        self.engine = create_engine("mysql+pymysql://root:Password123@localhost/teststand_recirculation",pool_pre_ping=True)
        self.azure = create_engine("mysql+pymysql://wojtek:Password#102@wojtek.mysql.database.azure.com/teststand_recirculation",pool_pre_ping=True)
        self.times = pd.read_sql_query("SELECT * FROM teststand_recirculation.times;", con = engine).drop("times_id", axis = 1)
        
    def details(self):
        self.info = self.times.loc[[self.value],:]
        # msgbox(self.details, ok_button="CLOSE")
        return self.info
    
    def slice_time(self):
        self.start = self.times.loc[self.value,"start"]
        self.end = self.times.loc[self.value,"end"]
        self.df_hobo = pd.read_sql_query("SELECT * FROM teststand_recirculation.recirculation WHERE datetime BETWEEN '{}' AND '{}'".format(self.start, self.end), con = self.engine)
        self.df_remus = pd.read_sql_query("SELECT * FROM teststand_recirculation.remus WHERE datetime BETWEEN '{}' AND '{}'".format(self.start, self.end), con = self.engine)
        return self.df_hobo, self.df_remus
 
    def plotly(self):
        self.df_hobo = self.slice_time()[0]
        self.df_remus = self.slice_time()[1]
        self.info = self.details()
        pd.options.plotting.backend = "plotly"

        import plotly.io as pio
        
        pio.renderers.default='browser'
        import plotly.express as px
        
       
        fig = px.line(self.df_hobo, x="datetime", y=self.df_hobo.columns, title=str(self.info.iloc[0,3:8]))
        # fig.add_annotation(dict(font=dict(color='black',size=15),
        #                                 x=0,
        #                                 y=-0.1,
        #                                 showarrow=False,
        #                                 text=str(self.details.iloc[0,3:8]),
        #                                 textangle=0,
        #                                 xanchor='left',
        #                                 xref="paper",
        #                                 yref="paper"))
        fig.show()
        
        
        import plotly.io as pio
        
        pio.renderers.default='browser'
        pd.options.plotting.backend = "matplotlib"
        #######################################################################
        pd.options.plotting.backend = "plotly"

        import plotly.io as pio
        
        pio.renderers.default='browser'
        import plotly.express as px
        
       
        fig = px.line(self.df_remus, x="datetime", y=self.df_remus.columns, title=str(self.info.iloc[0,3:8]))

        fig.show()
        
        
        import plotly.io as pio
        
        pio.renderers.default='browser'
        pd.options.plotting.backend = "matplotlib"
    

#%%

a = TestStand(10)
a.plotly()

#%%
# for i in range(15):
#     a = TestStand(i)
#     a.plotly()


























#%%