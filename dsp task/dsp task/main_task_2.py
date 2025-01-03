
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Button, simpledialog, messagebox


def display_signal(t_Discrete, signal_Discrete,t_Continuous,signal_Continuous, title):
    plt.figure()
    plt.plot(t_Continuous, signal_Continuous, label="Continuous")
    plt.scatter(t_Discrete, signal_Discrete, label="Discrete", color='red')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def generate_sine_wave(A, theta, analog_freq, sampling_freq, duration):
    n = np.arange(0, duration, 1/sampling_freq)
    sine_wave = A * np.sin(2 * np.pi * analog_freq * n + theta)
    return n, sine_wave

def generate_cosine_wave(A, theta, analog_freq, sampling_freq, duration):
    n = np.arange(0, duration, 1/sampling_freq)
    cosine_wave = A * np.cos(2 * np.pi * analog_freq * n + theta)
    return n, cosine_wave
