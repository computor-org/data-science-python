import numpy as np


def euler_symplectic(fun, dt, t_max, y_0):
    """
    input:
    fun: Function that describes the differential equation system
    dt: Step size
    t_max: End time
    y_0: Initial values as array [theta0, omega0]

    output:
    t: Array of time points
    y: Array of solutions [theta, omega] at time points t
    """
    t = np.arange(0, t_max + dt, dt)
    y = np.zeros((len(t), len(y_0)))
    y[0] = y_0

    for i in range(1, len(t)):
        y_prev = y[i - 1]
        omega_prev = y_prev[1]
        theta_next = y_prev[0] + dt * omega_prev + np.pi
        omega_next = (
            omega_prev + dt * np.array(fun(t[i - 1], [theta_next, omega_prev]))[1]
        )
        y[i] = [theta_next, omega_next]

    return t, y


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
