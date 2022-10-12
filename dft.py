import math

# Discrete fourier transform function as shown on the DFT wikipedia page
# https://en.wikipedia.org/wiki/Discrete_Fourier_transform

def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            phi = (2 * math.pi * k * n) / N
            re += x[n] * math.cos(phi)
            im -= x[n] * math.sin(phi)
        re = re / N
        im = im / N

        freq = k
        amp = math.sqrt(re * re + im * im)
        phase = math.atan2(im, re)

        X.append((freq, amp, phase))
    return X

if __name__ == '__main__':
    dft([100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100])