import os

cur_dir = os.path.dirname(__file__)
os.system(f"pytest {cur_dir}/test_polynom.py")
