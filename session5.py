import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from astropy.table import Table


# make array of values from 0 to 2pi with 1000 values
x = np.linspace(0, 2 * np.pi , 1000)

# we are looking for sin(x)
y = np.sin(x)

# create pairs containing our x and y values
table_entries = [(a, b) for a, b in zip(x, y)]

# make the table
table_headers = ["x","y"]
table = tabulate(table_entries, tablefmt="grid", headers=table_headers, floatfmt=".4f")


def main():
    print(table)

if __name__ == "__main__":
    main()