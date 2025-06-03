import numpy as np

import matplotlib.pyplot as plt

# Get user input for the formula
formula = input("Enter a formula in terms of x (e.g., abs(x), x.real**2 + x.imag**2, np.sin(x)): ")

# Define the grid for x (real) and y (imaginary)
x_real = np.linspace(-5, 5, 100)
x_imag = np.linspace(-5, 5, 100)
X_real, X_imag = np.meshgrid(x_real, x_imag)
Y = X_real + 1j * X_imag

# Evaluate the formula safely
try:
    # Only allow numpy and y in eval
    result = eval(formula, {"np": np, "x": Y})
except Exception as e:
    print(f"Error evaluating formula: {e}")
    exit(1)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_real, X_imag, np.real(result), cmap='viridis')

ax.set_xlabel('x (real)')
ax.set_ylabel('x (imaginary)')
ax.set_zlabel('Result (real part)')
plt.title(f"3D Graph of: {formula}")
plt.show()