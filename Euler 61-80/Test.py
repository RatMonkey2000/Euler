import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import TextBox

# Create a meshgrid for the complex plane with a 40x40 grid resolution
real_vals = np.linspace(-10, 10, 20)
imag_vals = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(real_vals, imag_vals)
Z = X + 1j * Y  # Complex plane meshgrid

# Define initial function: |z|^2
def initial_function(z):
    return np.abs(z)**2

# Plot setup
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Initial plot
output = initial_function(Z)
surface = ax.plot_surface(X, Y, output, cmap='viridis', edgecolor='none')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_zlabel('Output')
ax.set_title('Interactive 3D Plot of a Complex Function')

# Set 40x40x40 scale limits for the plot
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(0, 40)

# Color bar for the surface
cbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Function Output')

# Function to update the plot when a new function is entered
def update_plot(expression):
    global Z, surface, cbar
    try:
        # Evaluate the user-entered expression for Z
        new_output = eval(expression, {"z": Z, "np": np})

        # Clear the current plot and redraw with the new function
        ax.clear()
        surface = ax.plot_surface(X, Y, np.real(new_output), cmap='viridis', edgecolor='none')
        ax.set_xlabel('Real Part')
        ax.set_ylabel('Imaginary Part')
        ax.set_zlabel('Output')
        ax.set_title(f'3D Plot of {expression}')

        # Set limits for the updated plot
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_zlim(0, 40)

        # Update color bar
        if cbar:
            cbar.remove()
        cbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)
        cbar.set_label('Function Output')

        fig.canvas.draw_idle()
    except Exception as e:
        print(f"Error in expression: {e}")

# Add a text box widget to enter a new function
text_box_ax = plt.axes([0.2, 0.01, 0.6, 0.05])
text_box = TextBox(text_box_ax, 'Function (f(z)): ', initial='np.abs(z)**2')

# Update the plot whenever a new function is entered
text_box.on_submit(update_plot)

# Display the interactive plot
plt.show()