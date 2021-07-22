# A script that implements 2D simplex noise
# 2021, Dewi Payne

# Credit to Stefan Gustavson for the paper explaining the concept and sample java code,
# and Ken Perlin for originally creating the algorithm
# https://weber.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf
import random
import math


def random_noise():
    # Basic random noise, for comparison/reference
    return random.random()


def simplex_noise(x, y):
    # returns a value of 2-dimension simplex noise at a given point (x, y)

    # Contributions from the three corners of our 2d simplex triangles
    n0, n1, n2 = 0, 0, 0

    # Skewing the input to determine what cell we're in in the simplex grid
    skew_factor = (math.sqrt(3)-1)/2
    skew_amount = (x+y)*skew_factor
    # These give the cell we're in
    i = math.floor(x+skew_amount)
    j = math.floor(y+skew_amount)

    # un-skews the cells back to our original input space
    unskew_factor = (3-math.sqrt(3))/6
    unskew_amount = (i+j) * unskew_factor
    X0 = i - unskew_amount
    Y0 = j - unskew_amount
    x0 = x - X0
    y0 = y - Y0

    # Here we find what equilateral triangle we're in depending on if x or y is greater
    i1, j1 = (1, 0) if x0 > y0 else (0, 1)


if __name__ == '__main__':
    # Graphs the noise implementations
    x, y = [], []
    for i in range(100):
        x.append(random_noise())
        y.append(random_noise())  # Temporary, should be changed when simplex noise is implemented

    import matplotlib.pyplot as plt
    figure, axis = plt.subplots(2, sharex=True, sharey=True)

    axis[0].set_title("Random noise")
    axis[1].set_title("Simplex noise")

    axis[0].plot(x)
    axis[1].plot(y)

    plt.show()
