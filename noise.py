# A program that implements simplex noise
# 2021, Dewi Payne

# Credit to Stefan Gustavson for the paper explaining the concept, and Ken Perlin for originally creating it
# https://weber.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf
import random


def random_noise():
    # Basic random noise, for comparison/reference
    return random.random()


def simplex_noise(x, y):
    # returns a value of 2-dimension simplex noise at a given point (x, y)

    pass


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
