import math
import os
import numpy as np
from types import SimpleNamespace
from decimal import Decimal, getcontext


def read_specifications(filename):
    config = SimpleNamespace()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '=' in line:
                name, value = line.split('=', 1)
                name = name.strip()
                value = value.strip()
                try:
                    if '.' in value:
                        setattr(config, name, float(value))
                    else:
                        setattr(config, name, int(value))
                except ValueError:
                    setattr(config, name, value)
    return config

def lowpass(n,fc):
    wc = 2 * np.pi * fc
    if n == 0 :
        return 2*fc
    else:
        return 2 * fc * (np.sin(n * wc) / (n * wc))
    
def highpass(n,fc):
    wc = 2 * np.pi * fc
    if n == 0 :
        return 1 - 2*fc
    else:
        return -2 * fc * (np.sin(n * wc) / (n * wc))
    
def bandpass(n,fc1,fc2):
    wc1 = 2 * np.pi * fc1
    wc2 = 2 * np.pi * fc2
    if n == 0 :
        return 2*(fc2-fc1)
    else:
        return (2 * fc2 * (np.sin(n * wc2) / (n * wc2))) - (2 * fc1 * (np.sin(n * wc1) / (n * wc1)))
    
def bandreject(n,fc1,fc2):
    wc1 = 2 * np.pi * fc1
    wc2 = 2 * np.pi * fc2
    if n == 0 :
        return 1 - 2*(fc2-fc1)
    else:
        return (2 * fc1 * (np.sin(n * wc1) / (n * wc1)))-(2 * fc2 * (np.sin(n * wc2) / (n * wc2)))
    
def rectangular(n,N):
    return 1
def hanning(n,N):
   return 0.5+(0.5*math.cos((2*np.pi*n)/N))
def hamming(n,N):
    return 0.54+(0.46*math.cos((2*np.pi*n)/N))
def blackman(n,N):
    return 0.42+(0.5*math.cos((2*np.pi*n)/(N-1)))+(0.08*math.cos((4*np.pi*n)/(N-1)))

def get_filter(config):
    if config.StopBandAttenuation <= 21:
        setattr(config, "WindowType", "Rectangular")
        setattr(config, "N", config.FS*0.9/config.TransitionBand)
    elif config.StopBandAttenuation <= 44:
        setattr(config, "WindowType", "Hanning")
        setattr(config, "N", config.FS*3.1/config.TransitionBand)
    elif config.StopBandAttenuation <= 53:
        setattr(config, "WindowType", "Hamming")
        setattr(config, "N", config.FS*3.3/config.TransitionBand)
    else:
        setattr(config, "WindowType", "Blackman")
        setattr(config, "N", config.FS*5.5/config.TransitionBand)

    config.N=math.ceil(config.N)
    if int(config.N) % 2==0:
        config.N+=1

    indices = []
    values = []
    print(config.N)
    for n in range(int(-config.N/2),int((config.N/2)+1)):
        #filter
        if config.FilterType == "Low pass":
            h = lowpass(n,(config.FC+config.TransitionBand/2)/config.FS)
        elif config.FilterType == "High pass":
            h = highpass(n,(config.FC-config.TransitionBand/2)/config.FS)
        elif config.FilterType == "Band pass":
            h = bandpass(n,(config.F1-config.TransitionBand/2)/config.FS,(config.F2+config.TransitionBand/2)/config.FS)
        else:
            h = bandreject(n,(config.F1+config.TransitionBand/2)/config.FS,(config.F2-config.TransitionBand/2)/config.FS)

        #window
        if config.WindowType == "Rectangular":
            w = rectangular(n,config.N)
        elif config.WindowType == "Hanning":
            w = hanning(n,config.N)
        elif config.WindowType == "Hamming":
            w = hamming(n,config.N)
        else:
            w = blackman(n,config.N)
        
        indices.append(n)
        values.append(h*w)
    paired_lists = list(zip(indices, values))
    sorted_pairs = sorted(paired_lists, key=lambda pair: pair[0])
    indices, values = zip(*sorted_pairs)
    indices = list(indices)
    values = list(values)
        
    return (indices,values)

def apply_DFT_7(Signal1):
    time_values,signal_values = Signal1
    def dft(signal):
        N = len(signal)
        result = []
        for k in range(N):
            real = 0.0
            imag = 0.0
            for n in range(N):
                angle = -2 * math.pi * k * n / N
                real = signal[n] * math.cos(angle)
                imag = signal[n] * math.sin(angle)
                result.append(complex(real, imag))
        return result
    dft_result = dft(signal_values)
    return dft_result