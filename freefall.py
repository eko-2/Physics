import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from math import sqrt
import numpy as np
# Create a 2x1 grid of subplots
fig, axs = plt.subplots(2, 1)
plt.subplots_adjust(bottom=0.3,hspace=1)  # Adjust space for the textbox

# Define a callback function
# def submit(text):
#     print(f"Entered text: {text}")

a = 9.81
s = 0
t = 0
initialHeight = 0 
timeResolution = 0.1
u = 0
finalV = 0


running = True 
while running:
    
    initialHeight = int(input("What is the height of your object: "))
    try: 
        if initialHeight < 0:
            print("Please enter a positive number")
            continue
    except ValueError:
        continue

    timeTaken = sqrt((2*initialHeight)/9.81)
    print(f"Time taken: {timeTaken}")

    # Velocity time graph 
    xPoints = []
    yPoints = []

    finalV = u + (a*timeTaken) # final velocity at the very end. 
    for t in np.arange(0, timeTaken+timeResolution, timeResolution):
        v = u + (a*t)

        xPoints.append(t)
        yPoints.append(v)

    # Velocity time graph
    axs[0].plot(xPoints, yPoints)
    axs[0].set_title("Velocity-Time Graph")
    axs[0].set_xlabel("Time")
    axs[0].set_ylabel("Velocity")
    axs[0].legend("upper right")
    axs[0].grid(True)
    axs[0].set_xlim(0, timeTaken)
    axs[0].set_ylim(0, finalV)


    # DISPLACEMENT - TIME GRAPH         
    xPoints1 = []
    yPoints1 = []

    for t in np.arange(0, timeTaken+timeResolution, timeResolution): #isn't showing the create displacement. 
        s = (0*t)+((9.81*(t*t)/2))
        xPoints1.append(t)
        yPoints1.append(s)

    axs[1].plot(xPoints, yPoints)
    axs[1].set_title("Displacement-Time Graph")
    axs[1].set_xlabel("Time")
    axs[1].set_ylabel("Displacement")
    axs[1].legend("upper right")
    axs[1].grid(True)
    axs[1].set_xlim(0, timeTaken)
    axs[1].set_ylim(0, s)

    plt.show(block=False)
    plt.pause(0.5)
    axs[0].clear()




