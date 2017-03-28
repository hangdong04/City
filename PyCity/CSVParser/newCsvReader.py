import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py
import plotly

plotly.offline.init_notebook_mode()
import pandas as pd
from sklearn import svm, datasets

car = 'C:\\Users\phatt\Desktop\City\PyCity\Data\car_simu.txt'
motor = 'C:\\Users\phatt\Desktop\City\PyCity\Data\\bike_simu.txt'

car_data = pd.read_csv(car, header=0)
motor_data = pd.read_csv(motor, header=0)
# mean_speed  max_speed  mean_aclr  mean_upaclr  max_upaclr  mean_downaclr  #header
#
# print(car_data)
# print(car_data.mean_speed[0:100])
# print(len(car_data.index))

ind = list(range(100))
data_cplot = car_data.mean_speed[0:100]
data_mplot = motor_data.mean_speed[0:100]


import pandas as pd
df = pd.read_csv('http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt', sep='\t')
df2007 = df[df.year==2007]
df1952 = df[df.year==1952]
df.head(2)

fig = {
    'data': [
  		{
  			'x': data_cplot,
        	'y': data_cplot,
			'name':'Car',
        	'mode': 'markers'},
        {
        	'x': data_mplot,
        	'y': data_mplot,
			'name':'Motor',
        	'mode': 'markers'}
    ],
    'layout': {
        'xaxis': {'title': 'Mean speed'},
        'yaxis': {'title': "Mean speed"}
    }
}

# IPython notebook
# py.iplot(fig, filename='pandas/multiple-scatter')
plotly.offline.plot(fig, filename='multiple-scatter')