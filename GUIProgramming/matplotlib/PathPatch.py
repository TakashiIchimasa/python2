#! /usr/bin/env python2
# https://matplotlib.org/gallery/shapes_and_collections/path_patch.html
# above is referrenced but modified by Gocha.

import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
	(Path.MOVETO, ( 1.5, -2.6)),
	(Path.CURVE4, ( 0,4, -1.1)),
	(Path.CURVE4, ( -1.8, -2.0)),
	(Path.CURVE4, ( 0.38, 2.0)),
	(Path.LINETO, ( 0.85, 1.15)),
	(Path.CURVE4, ( 2.2, 3.2)),
	(Path.CURVE4, ( 3, 0.05)),
	(Path.CURVE4, ( 2.0, -0.5)),
	(Path.CLOSEPOLY, ( 1.58, -2.57)),
] 

codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

x,y = zip(*path.vertices)
line, = ax.plot(x,y,'go-')

ax.grid()
ax.axis('equal')
plt.show()

