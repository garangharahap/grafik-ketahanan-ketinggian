#Garang Anggi P Harahap (190170182)

import matplotlib.pyplot as plt
import numpy as np

#grafik jatuh bebas
h = np.arange(10,100,10)
g = 9.8
v = (2*g*h)**0.5

#grafik kecepatan - ketinggian
plt.plot(v,h, color="red", marker="x")
plt.title("Grafik Kecepatan - Ketinggian")
plt.xlabel("Kecepatan (m/s)")
plt.ylabel("Ketinggian (m)")
plt.grid()
plt.show()