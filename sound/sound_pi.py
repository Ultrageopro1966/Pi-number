import wave
import math
import struct

with open('pi.txt') as pi_num:
    pi_num = str(pi_num.read())

SR = 44100


def write_wave(filename, samples):
    f = wave.open(filename, "w")
    f.setparams((1, 2, SR, len(samples), "NONE", ''))
    f.writeframes(b"".join(
        [struct.pack('<h', round(x * 32767)) for x in samples]))
    f.close()

# Перевод секунд в количество сэмплов


def sec(x):
    return SR * x


def sines(bank, t):
    mix = 0
    for f in bank:
        mix += math.sin(2*math.pi * f * t / SR)
    return mix


# DTMF-сигналы для цифр 1-9
DTMF = [
    [100], [200], [300], [400], [500],
    [600], [700], [800], [900],
    [1000]
]

samples = []
nums = str(pi_num)[:3000]

for d in list(nums):
    for t in range(int(sec(0.025))):
        samples.append(sines(DTMF[int(d)], t))
    for t in range(int(sec(0.025))):
        samples.append(0)


write_wave("sound/dtmf.wav", samples)
