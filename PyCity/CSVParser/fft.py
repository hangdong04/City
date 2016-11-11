from CSVParser.Helper import Helper
import plotly.graph_objs as go
import plotly
from scipy.fftpack import fft
plotly.offline.init_notebook_mode()

# car_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Car.csv'
# motor_path = 'C:\\Users\Phatthanaphong\Desktop\City\PyCity\Data\Motorcycle.csv'

car_path = '/home/aaa/Desktop/City/PyCity/Data/Car.csv'
motor_path = '/home/aaa/Desktop/City/PyCity/Data/Motorcycle.csv'
Helper = Helper()

Car = Helper.reader(car_path)
car = Helper.preprocess(Car)
Motor = Helper.reader(motor_path)
motor = Helper.preprocess(Motor)
# print(car[0].get('speed'))

new_time = Helper.time_rescale(car[0].get('time'))

trace0 = go.Scatter(
    y = abs(fft(car[0].get('speed'))),
    mode = 'lines',
    name = 'lines'
)

trace1 = go.Scatter(
    y = abs(fft(motor[7].get('speed'))),
    mode = 'lines',
    name = 'lines'
)

data = [trace0]
layout = dict(title = 'FFT Speed of Car',
              xaxis = dict(title = 'Freq. (Hz.)'),
              yaxis = dict(title = 'Magnitude'),
              )
fig = dict(data = data, layout = layout)
plotly.offline.plot(fig, filename='fft-car-speed')


data1 = [trace1]
layout1 = dict(title = 'FFT Speed of Motorcycle',
              xaxis = dict(title = 'Freq. (Hz.)'),
              yaxis = dict(title = 'Magnitude'),
              )
fig1 = dict(data = data1, layout = layout1)
plotly.offline.plot(fig1, filename='fft-motor-speed')

trace2 = go.Scatter(
    y = abs(fft(car[0].get('bearing'))),
    mode = 'lines',
    name = 'lines'
)
data2 = [trace2]
layout2 = dict(title = 'FFT Head Change of Car',
               xaxis=dict(title='Freq. (Hz.)'),
              yaxis = dict(title = 'Magnitude'),
              )
fig2 = dict(data = data2, layout = layout2)
plotly.offline.plot(fig2, filename='fft-car-hcr')
trace3 = go.Scatter(
    y = abs(fft(motor[7].get('bearing'))),
    mode = 'lines',
    name = 'lines'
)
data3 = [trace3]
layout3 = dict(title = 'FFT Head Change of Motorcycle',
               xaxis=dict(title='Freq. (Hz.)'),
              yaxis = dict(title = 'Magnitude'),
              )
fig3 = dict(data = data3, layout = layout3)
plotly.offline.plot(fig3, filename='fft-motor-hcr')


