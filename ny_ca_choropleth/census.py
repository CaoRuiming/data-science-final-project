

import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='hyunchoi98', api_key='vYePaAgyDChhMTdXqPzM')

import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('caincome.csv')
# df_sample_r = df_sample[df_sample['techcode'] == 50]

values = df_sample['medianincome'].tolist()
fips = df_sample['County'].tolist()

colorscale = ["#FFFFFF","#E8E6F1","#D2CDE3","#BBB4d5","#a59bc8","#8e82ba",
              "#7869ac","#61509f","#4b3791","#341e83","#1e0576"]


fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    colorscale=colorscale,
    binning_endpoints=[45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000],
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Median Household Income by County', title='California'
)
py.plot(fig, filename='CAIncome')
