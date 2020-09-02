#! /usr/bin/env python2 
# https://matplotlib.org/gallery/subplots_axes_and_figures/subplot.html
# Inspired by above , but modified by Gocha to fit the purpose.

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace ( 0.0 , 5.0)
x2 = np.linspace ( 0.0 , 2.0)

y1 = np.cos(2* np.pi * x1) * np.exp(-x1)
y2 = np.cos(2* np.pi * x2) 

fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle('A tale of 2 subplots')

ax1.plot(x1,y1, 'o-')
ax1.set_ylabel('Damped oscillation')

ax2.plot(x1,y2, '.-')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')

plt.show()
