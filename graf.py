
import numpy as np
import matplotlib.pyplot as plt
import traceback
import matplotlib.gridspec as gridspec
from matplotlib import rcParams
import matplotlib.ticker as ticker
import datetime
from scipy.fftpack import fft
from math import pi


data_S = np.loadtxt('settings.txt', dtype = float)
data = np.loadtxt ('data.txt', dtype=int)

data = data*4/255
L_A = len(data)
fig_data = plt.figure()

x_A = list(range(0, L_A))
x_A = [i/100 for i in x_A]


subplot_data_A = fig_data.add_subplot(111)

# subplot_data_A.set_xticklabels('')
subplot_data_A.set_ylabel(u'Voltage, V')
subplot_data_A.set_xlabel(u'Time, s')

# max_A = max(data_A['data'])
# min_A = min(data_A['data'])
# min_A_border = min_A-5

# plt.axis([0,160, min_A_border, max_A])
subplot_data_A.set_title('Voltage vs time')

line_data_A = subplot_data_A.plot(x_A, data, marker = '*', color='blue', linewidth=2, label = 'voltage', markevery=30)
subplot_data_A.legend()

for ax in fig_data.axes:
    ax.grid(True)
subplot_data_A.text(5.5,2.5, 'Time of charge: 4.20 s')
subplot_data_A.text(5.5,2, 'Time of discharge: 5.7 s')
plt.show()

fig_data.savefig('/home/gr105/Desktop/Scripts/fedorova/fig', format = 'svg')