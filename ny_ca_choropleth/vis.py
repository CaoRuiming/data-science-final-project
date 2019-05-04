import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='hyunchoi98', api_key='vYePaAgyDChhMTdXqPzM')

import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('cagigabit.csv')
# df_sample_r = df_sample[df_sample['techcode'] == 50]

values = df_sample['avgspeed'].tolist()
fips = df_sample['County'].tolist()

colorscale = [
    'rgb(193, 193, 193)',
    'rgb(239,239,239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    colorscale=colorscale,
    binning_endpoints=[10, 50, 100, 500, 1000],
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Avg Gigabit (Fiber + DOCSIS 3.1) Speed by County', title='California'
)
py.plot(fig, filename='CAGigabit')
