import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button, TextBox

# Function to generate a default 3D plot
def plot_3d(ax, func, x_range, y_range, resolution=50):
    ax.clear()
    x = np.linspace(*x_range, resolution)
    y = np.linspace(*y_range, resolution)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.8)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.draw()

# Function for evaluating user-defined equations
def evaluate_function(equation, x, y):
    try:
        z = eval(equation)
    except Exception as e:
        z = np.zeros_like(x)
        print(f"Error evaluating function: {e}")
    return z

# Callback for updating the plot
def update_plot(event):
    equation = textbox.text
    plot_3d(ax, lambda x, y: evaluate_function(equation, x, y), (-10, 10), (-10, 10))

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

# Add buttons and textbox for user interaction
textbox_ax = plt.axes([0.1, 0.05, 0.7, 0.075])
textbox = TextBox(textbox_ax, "Enter function z=f(x,y): ", initial="x**2 - y**2")

button_ax = plt.axes([0.85, 0.05, 0.1, 0.075])
button = Button(button_ax, 'Plot')

# Plot default function
plot_3d(ax, lambda x, y: x**2 - y**2, (-10, 10), (-10, 10))

# Set button callback
button.on_clicked(update_plot)

# Display the interactive plot
plt.show()

