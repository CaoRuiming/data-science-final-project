import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='hyunchoi98', api_key='vYePaAgyDChhMTdXqPzM')

import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('caeduc.csv')
# df_sample_r = df_sample[df_sample['techcode'] == 50]

values = df_sample['bachelorsorgreater'].tolist()
fips = df_sample['County'].tolist()

colorscale = ["#E8E6F1","#BBB4d5","#8e82ba",
              "#7869ac","#4b3791","#341e83","#1e0576"]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    colorscale=colorscale,
    binning_endpoints=[10, 20, 30, 40, 50, 60],
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Percentage of People with Degrees Bachelors or Higher by County', title='California'
)
py.plot(fig, filename='CAEduc')
