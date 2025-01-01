import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from math import sqrt
# Create a 2x1 grid of subplots
fig, axs = plt.subplots(2, 1)
plt.subplots_adjust(bottom=0.3)  # Adjust space for the textbox

# Define a callback function
def submit(text):
    print(f"Entered text: {text}")


# so lets plot
xPoints = []
yPoints = []

# SUVAT
u = 0
for i in range(11):
    t = i 
    v = u + 9.81*t
    u = v
    xPoints.append(t)
    yPoints.append(v)

axs[0].plot(xPoints, yPoints)

# Velocity time graph
axs[0].set_title("Velocity-Time Graph")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Velocity")
axs[0].legend("upper right")
axs[0].grid(True)
axs[0].set_xlim(0, 10)
axs[0].set_ylim(0, 40)

# xPoints1 = []
# yPoints1 = []

# for i in range(11):
#     t = i
#     a = 9.81
#     xPoints1.append(t)
#     yPoints1.append(a)

# axs[1].plot(xPoints, yPoints)

# axs[1].set_title("Acceleration-Time Graph")
# axs[1].set_xlabel("Time")
# axs[1].set_ylabel("Acceleration")
# axs[1].legend("upper right")
# axs[1].grid(True)
# axs[1].set_xlim(0, 10)
# axs[1].set_ylim(0, 40)

# Display the window
plt.show()
