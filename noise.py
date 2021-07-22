# A program that implements simplex noise
# 2021, Dewi Payne

# Credit to Stefan Gustavson for the paper explaining the concept, and Ken Perlin for originally creating it
# https://weber.itn.liu.se/~stegu/simplexnoise/simplexnoise.pdf


import random


def random_noise():
    # Basic random noise, for comparison/reference
    return random.random()


def simplex_noise(x):
    # returns a sample value of 1-dimension perlin noise at a given time x

    pass


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    noise_list = []

    for i in range(10):
        noise_list.append(simplex_noise(i))

    plt.plot(noise_list)
    plt.show()
