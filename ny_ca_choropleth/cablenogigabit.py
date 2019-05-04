import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='hyunchoi98', api_key='vYePaAgyDChhMTdXqPzM')

import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('cacablenogigabit.csv')
# df_sample_r = df_sample[df_sample['techcode'] == 50]

values = df_sample['avgspeed'].tolist()
fips = df_sample['County'].tolist()

colorscale = ["#E8E6F1","#D2CDE3","#BBB4d5","#a59bc8","#8e82ba",
              "#7869ac","#61509f","#4b3791","#341e83","#1e0576"]


fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    colorscale=colorscale, show_state_data=True,
    binning_endpoints=[50, 100, 150, 200, 250, 300, 350],
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Speed of Cable Providers by County', title='California'
)
py.plot(fig, filename='CACableNoGigabit')
