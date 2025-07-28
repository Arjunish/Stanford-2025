import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)

line1, = ax.plot(x, np.zeros_like(x), color = 'white')
line2, = ax.plot(x, np.zeros_like(x), color = 'white')
line3, = ax.plot(x, np.zeros_like(x), color='green')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

a1, w1, k1 = 1, 2 * np.pi, 0
a2, w2, k2 = 0.6, 3 * np.pi, np.pi / 4

def update(frame):
    t = frame  
    y1 = a1 * np.sin(w1 * x + k1 + t)
    y2 = a2 * np.sin(w2 * x + k2 + t)
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y1 * y2)
    return (line1, line2, line3)

ani = animation.FuncAnimation(fig, update, frames=150, interval=100, blit=True)
plt.show()


