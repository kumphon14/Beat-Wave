import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
v = 300  # Velocity
f1 = 150  # Frequency of wave1
f2 = 170  # Frequency of wave2

k1 = (2 * np.pi * f1) / v  # Wave1 number
k2 = (2 * np.pi * f2) / v  # Wave2 number
A = 2  # Amplitude
x = np.linspace(0, 20 * np.pi, 1000)  # x range (extended for Beat clarity)

# Node positions for Beat Wave
node_positions = [-1 * np.pi / (k1 - k2), -3 * np.pi / (k1 - k2), -5 * np.pi / (k1 - k2)]

# Initialize figure and axes
fig, (ax1, ax2, axB) = plt.subplots(3, 1, figsize=(12, 10))  # Three subplots

# Wave 1
line1, = ax1.plot(x, A * np.sin(k1 * x), color="blue", label="Wave 1")
ax1.set_ylim(-A - 1, A + 1)  # Set y-axis limits
ax1.set_title("Wave 1 Animation")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(color='lightgray', linestyle='--', linewidth=0.5)  # Add grid for Wave 1
ax1.legend(loc='upper right')

# Wave 2
line2, = ax2.plot(x, A * np.sin(k2 * x), color="red", label="Wave 2")
ax2.set_ylim(-A - 1, A + 1)  # Set y-axis limits
ax2.set_title("Wave 2 Animation")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(color='lightgray', linestyle='--', linewidth=0.5)  # Add grid for Wave 2
ax2.legend(loc='upper right')

# Beat Wave (Superposition)
lineBeat, = axB.plot(x, A * np.sin(k1 * x) + A * np.sin(k2 * x), color="black", label="Beat Wave")
axB.set_ylim(-2 * A - 1, 2 * A + 1)  # Set y-axis limits to handle superposition
axB.set_title("Beat Wave Animation with Nodes")
axB.set_xlabel("x")
axB.set_ylabel("y")
axB.grid(color='lightgray', linestyle='--', linewidth=0.5)  # Add grid for Beat Wave

# Add vertical dashed lines at Node positions
for node in node_positions:
    axB.axvline(x=node, color='green', linestyle='--', linewidth=2, label="Node" if node == node_positions[0] else "")

# Update function
def waveLine(frame):
    y1 = A * np.sin(k1 * x - frame)  # Add time dependency for wave1
    y2 = A * np.sin(k2 * x + frame)  # Add time dependency for wave2
    y_beat = y1 + y2  # Superposition for Beat Wave
    line1.set_ydata(y1)  # Update Wave 1
    line2.set_ydata(y2)  # Update Wave 2
    lineBeat.set_ydata(y_beat)  # Update Beat Wave
    return line1, line2, lineBeat

# Animation
tp = np.linspace(0, 2 * np.pi, 150)  # Time frames
animation = FuncAnimation(fig, waveLine, frames=tp, interval=50, blit=True)

# Add legend for Nodes
axB.legend(loc='upper right')

# Show animation
plt.tight_layout()
plt.show()
