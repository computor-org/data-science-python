"""Public runtime checks; exercise grading remains a separate authenticated task."""
import io
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp


def test_numeric_environment_solves_known_decay():
    result = solve_ivp(lambda t, y: -y, (0, 1), [1.0], rtol=1e-8, atol=1e-10)
    assert abs(result.y[0, -1] - np.exp(-1)) < 1e-8


def test_headless_plot_environment_creates_valid_png():
    fig, ax = plt.subplots()
    try:
        ax.plot([0, 1], [1, 0])
        output = io.BytesIO()
        fig.savefig(output, format="png")
        assert output.getvalue().startswith(b"\x89PNG\r\n\x1a\n")
        assert len(output.getvalue()) > 1000
    finally:
        plt.close(fig)
