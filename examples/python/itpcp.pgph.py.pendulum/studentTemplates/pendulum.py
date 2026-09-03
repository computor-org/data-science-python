import numpy as np


def pendulum_ode(t, y, L=3.0, g=9.81):
    """
    input:
    t: Current time point
    y: Array [theta, omega], consisting of the current angle and angular velocity
    g: Gravitational constant (default: 9.81 m/s^2)
    L: Length of the pendulum (default: 1.0 m)

    output:
    Array [omega, - (g / L) * np.sin(theta)], representing the first derivative of theta and omega respectively
    """
    theta, omega = y
    return [omega, -(g / L) * np.sin(theta)]
