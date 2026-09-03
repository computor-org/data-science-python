import os
import sys

import numpy as np

# set path to filepath of current file
cur_file_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../itpcp.pgph.py.quadratic_eq_eval/")
sys.path.append("../itpcp.pgph.py.quadratic_eq/")
from quadratic_eq import quadratic_eq  # ! must be placed after sys.path.append
from quadratic_eq_eval import quadratic_eq_eval  # ! must be placed after sys.path.append


def quadratic_eq_test(n=16, rmin=3, rmax=6):
    """Test function for quadratic equation solver.

    Parameters:
    n: size of the matrices (default 16)
    rmin: minimum random value (default 3)
    rmax: maximum random value (default 6)

    Returns:
    x1, x2: solutions from quadratic_eq
    r1, r2: residuals from quadratic_eq_eval
    """
    #...
    pass
