import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Button, simpledialog, messagebox
from main_task_1 import *
from signalcompare import *
def apply_DFT(sampling_freq,Signal1):
    time_values,signal_values = Signal1
    def dft(signal):
        N = len(signal)
        result = []
        for k in range(N):
            sum_real = 0.0
            sum_imag = 0.0
            for n in range(N):
                angle = -2 * math.pi * k * n / N
                sum_real += signal[n] * math.cos(angle)
                sum_imag += signal[n] * math.sin(angle)
            result.append(complex(sum_real, sum_imag))
        return result
    dft_result = dft(signal_values)
    N = len(signal_values)
    frequencies = [k * sampling_freq / N for k in range(N)]
    amplitude = [abs(value) for value in dft_result]
    phase = [cmath.phase(value) for value in dft_result]


    # amp_test,phase_test = ReadSignalFile("./Output_Signal_DFT.txt")
    # if  SignalComapreAmplitude(amplitude,amp_test) and SignalComaprePhaseShift(phase,phase_test):
    #     print("DFT Passed successfully")
    # else:
    #     print("DFT didn't pass")

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.stem(frequencies, amplitude, basefmt=" ")
    plt.title("Frequency vs Amplitude")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid()

    
    plt.subplot(1, 2, 2)
    plt.stem(frequencies, phase, basefmt=" ")
    plt.title("Frequency vs Phase")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (radians)")
    plt.grid()

    plt.tight_layout()
    plt.show()
    # print((amplitude,phase))
    return dft_result,amplitude,phase


def apply_IDFT(dft_result):
    # Use the passed dft_result directly
    def idft(dft_result):
        N = len(dft_result)
        result = []
        for n in range(N):
            sum_value = complex(0, 0)
            for k in range(N):
                angle = 2 * math.pi * k * n / N
                exp_factor = complex(math.cos(angle), math.sin(angle))
                sum_value += dft_result[k] * exp_factor
            result.append(sum_value / N)
        return result

    # Perform IDFT
    reconstructed_signal = idft(dft_result)

    # Read expected signal for comparison
    # amp_test, phase_test = ReadSignalFile("./Output_Signal_IDFT.txt")

    # Prepare reconstructed signal for comparison
    reconstructed_indices = list(range(len(reconstructed_signal)))
    reconstructed_values = [value.real for value in reconstructed_signal]

    # Debugging prints
    # print("Reconstructed Indices:", reconstructed_indices)
    # print("Reconstructed Values:", reconstructed_values)
    # print("Expected Indices:", amp_test)
    # print("Expected Values:", phase_test)

    # Compare signals
    # if SignalComapreAmplitude(reconstructed_indices, amp_test) and SignalComaprePhaseShift(reconstructed_values, phase_test):
    #     print("IDFT Passed successfully")
    # else:
    #     print("IDFT didn't pass")

    # Return reconstructed signal
    return reconstructed_indices, reconstructed_values



def ReadSignalFile(file_name):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = float(L[0].replace('f','').strip())
                V2 = float(L[1].replace('f','').strip())
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    return expected_indices, expected_samples