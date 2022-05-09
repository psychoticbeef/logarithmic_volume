#!/usr/bin/env python3
import math
duration = 500

# dynamic range = 60 db
# values taken from: https://www.dr-lex.be/info-stuff/volumecontrols.html
a = 1e-3
b = 6.908

# fadein, 60 steps, 1 db per step
r = range(61)
for n in r:
    x = n/60.0
    # linear at low volume
    if x == 0:
        amplitude_factor = x*10
    # exponential otherwise
    else:
        amplitude_factor = a*math.exp(b*x)
    # clamp at 1, as formula is close, but not perfect
    if amplitude_factor > 1:
        amplitude_factor = 1
    print(amplitude_factor)

