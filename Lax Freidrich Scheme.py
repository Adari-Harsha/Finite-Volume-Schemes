import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial condition
def u0(x):
    return np.where(abs(x) <= 1, 1.0, 0.0)

# Spatial domain [-L, L] and time [0, T]
L = 5.0
T = 2.0
c = 2.0
# Discretization parameters h, dt
h = 0.1
dt = 0.025

# Grid ratio
gam = dt / h

# Number of space and time steps
n = int(2 * L / h) + 1
m = int(T / dt)

x = np.linspace(-L, L, n)
u = u0(x)

u_all_time_steps = []

u_all_time_steps.append(u.copy())

for t in np.linspace(dt, T, m):
    u[1:-1] = (u[2:] + u[:-2]) /  2 - c * gam * (u[2:] - u[:-2]) / 2
    u[0] = (u[1] + u[-1]) / 2 - c * gam * (u[1] - u[-1]) / 2
    u[-1] = (u[-1] + u[-2]) / 2 - c *  gam * (u[0] - u[-2]) / 2
    u_all_time_steps.append(u.copy())

fig, ax = plt.subplots()
ax.set(xlim=(-L, L), ylim=(-1, 2), xlabel='x', ylabel='u')
ax.set_title('Lax Freidrich Scheme')
line, = ax.plot([], [], 'b-')
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('Time = 0.00')
    return line, time_text

def animate(i):
    line.set_data(x, u_all_time_steps[i])
    time_text.set_text(f'Time = {i * dt:.3f} s')  
    return line, time_text

anim = FuncAnimation(fig, animate, init_func=init, frames=len(u_all_time_steps),
                     interval=50, blit=True)

plt.show()
