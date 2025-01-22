# Plotting the Random Walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()  # This will now work

# Plotting the points
plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.show()


#Generating Multiple random walks

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    
    # Scatter plot the walk points
    plt.scatter(rw.x_values, rw.y_values, s=15)
    
    # Show the plot
    plt.show()

    # Ask user if they want to make another walk
    keep_running = input("Make another walk? (y/n): ")
    
    if keep_running == 'n':
        break


# Styling: Coloring the points

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    
    # Generate point numbers for coloring
    point_numbers = list(range(rw.num_points))
    
    # Plot the random walk points with color mapping
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=15)
    
    # Display the plot
    plt.show()

    # Ask if the user wants to make another walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
