import numpy as np
from matplotlib import pyplot as plt

from statistics import mean

from scipy.io.wavfile import write

from scipy.fftpack import fft, fftfreq, rfft, rfftfreq, irfft

with open('data.txt') as f:
    # работа с файлом
    x1 = [float(line.strip()) for line in f]  # считывание исходных данных x1(t)

x_mean=mean(x1)  # находим среднее значение сигнала
print(x_mean)

x=[z-x_mean for z in x1]  # вычитаем среднне значение из исходного сигнала. x(t) = x1-x_mean

#print(x)

T=0.01 # Шаг дискретизации по времени. Важно ЗНАТЬ!!! Т.к. на основе этого вычисляются частоты спектра.

N=len(x)
t=[T*i for i in range(N)]  # время

#print(t)

plt.plot(t, x)  # график сигнала x(t) = x1-x_mean
plt.show()

X = rfft(x)          # вычисление амплитуд спектра.
f = rfftfreq(N, T)   # вычисление частот спектра. Диапазон [0, 1/(2T)]

#print(f)

X_abs=list(np.abs(X))

iMax=X_abs.index(max(X_abs))
print("Max f = ", f[iMax])     # Частота с максимальной амплитудой, т.е. с максимальным вкладом

plt.plot(f, X_abs)
plt.show()