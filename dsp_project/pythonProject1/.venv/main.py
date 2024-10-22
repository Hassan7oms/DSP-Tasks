import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Button, simpledialog, messagebox

def read_signal(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        indices = []
        values = []
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2:
                index, value = map(float, parts)
                indices.append(index)
                values.append(value)
            else:
                print(f"Skipping malformed line: {line.strip()}")
    return np.array(indices), np.array(values)

def save_signal(indices, values, filename="output_signal.txt"):
    with open(filename, 'w') as f:
        f.write(f"{len(indices)}\n")  # First line is the number of samples
        for index, value in zip(indices, values):
            f.write(f"{index} {value}\n")  # Each line contains an index and a value
    print(f"Signal saved to {filename}")

def display_signal(indices, values, title="Signal"):
    plt.figure()
    plt.stem(indices, values, basefmt=" ")
    plt.title(title)
    plt.xlabel('Index (n)')
    plt.ylabel('Amplitude')
    plt.show()

def add_signals(signals_list):
    # Get all unique indices from the signals
    all_indices = np.unique(np.concatenate([indices for indices, values in signals_list]))

    # Initialize an array to store the result signal
    result_signal = np.zeros(len(all_indices))

    # Add values from each signal to the result signal
    for indices, values in signals_list:
        for i, index in enumerate(all_indices):
            if index in indices:
                result_signal[i] += values[np.where(indices == index)[0][0]]

    return all_indices, result_signal


def apply_multiplication(indices, values, constant):
    return indices, values * constant

def apply_shift(indices, values, k):
    shifted_indices = indices + k
    return shifted_indices, values

def apply_reverse(indices, values):
    reversed_indices = -indices
    return reversed_indices, values
