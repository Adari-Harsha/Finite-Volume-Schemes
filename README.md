# Numerical Solutions and Animations of Advection Schemes

This repository contains Python code for solving and animating the advection equation using various numerical schemes. The schemes implemented include:

*   **Upwind Scheme**
*   **Downwind Scheme**
*   **Lax-Friedrich Scheme**
*   **Näive Scheme**

## Overview

The advection equation is a fundamental equation in physics that describes the transport of a scalar quantity (e.g., density, temperature) by a velocity field. Numerical schemes are used to approximate the solution of this equation on a discrete grid.

This repository provides implementations of several common numerical schemes for the 1D advection equation, along with visualizations of their behavior.

## Code Description

Each scheme is implemented in a separate Python file (e.g., `upwind_scheme.py`, `lax_friedrich_scheme.py`). The code uses the following libraries:

*   `numpy`: For numerical computations [1-4].
*   `matplotlib`: For plotting and animation [1-4].
*   `matplotlib.animation`: For creating animations [1-4].

### Common Parameters

The following parameters are used in all the schemes:

*   `L`: Length of the spatial domain, which is `[-L, L]` [1-4].
*   `T`: Final time [1-4].
*   `c`: Advection speed [2, 4].
*   `h`: Spatial step size [1-4].
*   `dt`: Time step size [1-4].
*   `gam`: Grid ratio, defined as `dt / h` [1-4].
*   `n`: Number of spatial grid points [1-4].
*   `m`: Number of time steps [1-4].

### Initial Condition

The initial condition is defined as a box function:

```python
def u0(x):
    return np.where(abs(x) <= 1, 1.0, 0.0)
This function sets the initial value to 1.0 for |x| <= 1 and 0.0 otherwise.
Numerical Update
The core of each scheme is the update rule applied at each time step. For example, the Lax-Friedrichs scheme updates the solution as follows:
u[1:-1] = (u[2:] + u[:-2]) / 2 - c * gam * (u[2:] - u[:-2]) / 2
u = (u[4] + u[-1]) / 2 - c * gam * (u[4] - u[-1]) / 2
u[-1] = (u[-1] + u[-2]) / 2 - c * gam * (u - u[-2]) / 2
The update rules for the other schemes can be found in their respective files.
Animation
Each scheme generates an animation of the solution over time using matplotlib.animation.FuncAnimation.  The animation displays the solution u(x) at different time steps.
Usage
To run a specific scheme, simply execute the corresponding Python file:
python upwind_scheme.py
This will generate an animation of the solution.  Ensure you have the required libraries installed (numpy and matplotlib).
Notes
•
The choice of h and dt can significantly affect the stability and accuracy of the numerical solution.
•
The boundary conditions are periodic.
•
The animation speed can be adjusted by changing the interval parameter in the FuncAnimation function
