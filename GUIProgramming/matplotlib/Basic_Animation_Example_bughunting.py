#! /usr/bin/env python2
# https://matplotlib.org/examples/animation/basic_example.html
# inspired by above, but modified by Gocha for purpose.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num , data, line):
	line.set_data(data [..., :num])
	return line,

fig1 = plt.figure()
data = np.random.rand(2,25)
#bug l = plt.plot([], [] , 'r-')
l, = plt.plot([], [] , 'r-')
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l), interval = 50, blit=True)
fig2= plt.figure()

x = np.arange(-9 , 10)
y = np.arange(-9 , 10).reshape(-1,1)
base = np.hypot(x,y)
ims = []

for add in np.arange(15):
	ims.append((plt.pcolor(x,y, base+add , norm = plt.Normalize(0,30)),))

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=300, blit=True)
plt.show()


	

