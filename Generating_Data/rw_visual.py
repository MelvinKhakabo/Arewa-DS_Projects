# Plotting the Random Walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()  # This will now work

# Plotting the points
plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.show()
