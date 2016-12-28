import numpy as np
import matplotlib.pyplot as plt

def main():
    a, b, klen = -2, 13, 103
    # a, b, klen = -1, 1, 97
    y, x = np.ogrid[0:klen:100j, 0:klen:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    # plt.plot([19, 27], [97, 81])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()


# https://jeremykun.com/2014/02/08/introducing-elliptic-curves/
