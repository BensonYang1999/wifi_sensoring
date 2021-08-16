import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import time

def load_data(filename):
    raw = np.genfromtxt(filename, delimiter=',')
    raw = raw[:-1]
    #print(raw)
    #print(raw.shape)
    return raw

def draw(raw):
    plt.figure(2, figsize=(20,16))
    f1 = plt.plot(raw)


TX = 1
RX = 3
#while True:
#filename = "test/csv" + str(TX) + "x" + str(RX) + ".csv"
#raw = load_data(filename)
#draw(raw)

plt.axis([0, 10, 0, 1])
while True:
    for i in range(10):
        y = np.random.random()
        plt.scatter(i, y)

    plt.show()
