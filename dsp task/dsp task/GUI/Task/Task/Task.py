import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import numpy as np
import QuanTest1
import QuanTest2

# Global variables for Task 1
Signal1 = None
Signal2 = None
Signal3 = None

### Styling Variables ###
BG_COLOR = "#2E2E2E"
FG_COLOR = "#00FF00"  # Green color for GUI text
BTN_BG = "#3C3C3C"
BTN_FG = "#00FF00"  # Green text on buttons
ENTRY_BG = "#4A4A4A"
ENTRY_FG = "#00FF00"  # Green text in entry fields
FONT = ("Arial", 12, "bold")


### Task 1 Functions ###

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
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    return expected_indices, expected_samples


def prepare_signals(signal1, signal2):
    indices1, amplitudes1 = signal1
    indices2, amplitudes2 = signal2

    all_indices = sorted(set(indices1).union(set(indices2)))
    new_amplitudes1 = [amplitudes1[indices1.index(i)] if i in indices1 else 0 for i in all_indices]
    new_amplitudes2 = [amplitudes2[indices2.index(i)] if i in indices2 else 0 for i in all_indices]

    return all_indices, new_amplitudes1, new_amplitudes2


def PlotSignal(Signal, title="Signal Plot"):
    indices, samples = Signal
    plt.figure(figsize=(10, 6))
    plt.plot(indices, samples, marker='o', linestyle='-', color='b', label="Signal")
    plt.title(title, fontsize=16, color='black')
    plt.xlabel('Index', fontsize=14, color='black')
    plt.ylabel('Amplitude', fontsize=14, color='black')
    plt.grid(True, color='gray')
    plt.legend(loc='lower left', fontsize=12, facecolor='white', edgecolor='black')
    plt.gca().set_facecolor("white")
    plt.gcf().patch.set_facecolor("white")
    plt.show()


def AddSignals(Signal1, Signal2):
    indices, amplitudes1 = Signal1
    _, amplitudes2 = Signal2
    added_amplitudes = [a1 + a2 for a1, a2 in zip(amplitudes1, amplitudes2)]
    ResultSignal = (indices, added_amplitudes)
    PlotSignal(ResultSignal, title="Added Signal")
    return ResultSignal


def SubtractSignals(Signal1, Signal2):
    indices, amplitudes1 = Signal1
    _, amplitudes2 = Signal2
    subtracted_amplitudes = [a1 - a2 for a1, a2 in zip(amplitudes1, amplitudes2)]
    ResultSignal = (indices, subtracted_amplitudes)
    PlotSignal(ResultSignal, title="Subtracted Signal")
    return ResultSignal


def MultiplySignal(signal, constant):
    indices, amplitudes = signal
    Multiplied_amplitudes = [a * constant for a in amplitudes]
    ResultSignal = (indices, Multiplied_amplitudes)
    PlotSignal(ResultSignal, title=f"Multiplied Signal by {constant}")
    return ResultSignal


def FoldSignal(signal):
    indices, samples = signal
    folded_indices = [-i for i in reversed(indices)]
    folded_samples = list(reversed(samples))
    ResultSignal = (folded_indices, folded_samples)
    PlotSignal(ResultSignal, title="Folded Signal")
    return ResultSignal


def DelaySignal(signal, k):
    indices, amplitudes = signal
    delayed_indices = [n + k for n in indices]
    ResultSignal = (delayed_indices, amplitudes)
    PlotSignal(ResultSignal, title=f"Delayed Signal by {k} steps")
    return ResultSignal


def AdvanceSignal(signal, k):
    indices, amplitudes = signal
    advanced_indices = [n - k for n in indices]
    ResultSignal = (advanced_indices, amplitudes)
    PlotSignal(ResultSignal, title=f"Advanced Signal by {k} steps")
    return ResultSignal


### Load and Operation Functions for Task 1 ###

def load_signal1():
    global Signal1
    file_path = filedialog.askopenfilename(title="Select Signal 1 File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        Signal1 = ReadSignalFile(file_path)
        messagebox.showinfo("Success", "Signal 1 Loaded Successfully!")


def load_signal2():
    global Signal2
    file_path = filedialog.askopenfilename(title="Select Signal 2 File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        Signal2 = ReadSignalFile(file_path)
        messagebox.showinfo("Success", "Signal 2 Loaded Successfully!")


def add_signals():
    if Signal1 and Signal2:
        indices, amp1, amp2 = prepare_signals(Signal1, Signal2)
        newSignal1 = (indices, amp1)
        newSignal2 = (indices, amp2)
        AddSignals(newSignal1, newSignal2)
    else:
        messagebox.showwarning("Error", "Please load both Signal 1 and Signal 2!")


def subtract_signals():
    if Signal1 and Signal2:
        indices, amp1, amp2 = prepare_signals(Signal1, Signal2)
        newSignal1 = (indices, amp1)
        newSignal2 = (indices, amp2)
        SubtractSignals(newSignal1, newSignal2)
    else:
        messagebox.showwarning("Error", "Please load both Signal 1 and Signal 2!")


def multiply_signal():
    if Signal1:
        constant = simpledialog.askfloat("Input", "Enter the multiplication constant:")
        if constant is not None:
            MultiplySignal(Signal1, constant)
    else:
        messagebox.showwarning("Error", "Please load Signal 1!")


def fold_signal():
    if Signal1:
        FoldSignal(Signal1)
    else:
        messagebox.showwarning("Error", "Please load Signal 1!")


def delay_signal():
    if Signal1:
        steps = simpledialog.askinteger("Input", "Enter delay steps (k):")
        if steps is not None:
            DelaySignal(Signal1, steps)
    else:
        messagebox.showwarning("Error", "Please load Signal 1!")


def advance_signal():
    if Signal1:
        steps = simpledialog.askinteger("Input", "Enter advance steps (k):")
        if steps is not None:
            AdvanceSignal(Signal1, steps)
    else:
        messagebox.showwarning("Error", "Please load Signal 1!")


### Task 1 GUI ###

def open_task1():
    task1_window = tk.Toplevel()
    task1_window.geometry("400x600")
    task1_window.title("Task 1 - Signal Operations")
    task1_window.configure(bg=BG_COLOR)

    # Load Signal Buttons
    tk.Button(task1_window, text="Load Signal 1", command=load_signal1, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=5)
    tk.Button(task1_window, text="Load Signal 2", command=load_signal2, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=5)

    # Operation Buttons
    tk.Button(task1_window, text="Add Signals", command=add_signals, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=5)
    tk.Button(task1_window, text="Subtract Signals", command=subtract_signals, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(
        pady=5)
    tk.Button(task1_window, text="Multiply Signal", command=multiply_signal, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(
        pady=5)
    tk.Button(task1_window, text="Fold Signal", command=fold_signal, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=5)
    tk.Button(task1_window, text="Delay Signal", command=delay_signal, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=5)
    tk.Button(task1_window, text="Advance Signal", command=advance_signal, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=5)

    # Back to Main Menu Button
    tk.Button(task1_window, text="Back to Main Menu", command=task1_window.destroy, bg=BTN_BG, fg=BTN_FG,
              font=FONT).pack(pady=20)


### Task 2 GUI ###

def plot_signals(amplitude, frequency, duration, phase_shift, sampling_frequency, plot_sine, plot_cosine):
    # Validate sampling frequency
    if sampling_frequency < 2 * frequency:
        messagebox.showerror("Error", "Sampling frequency must be at least 2 times the signal frequency!")
        return

    t_continuous = np.linspace(0, duration, 1000)
    t_discrete = np.arange(0, duration, 1 / sampling_frequency)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    if plot_sine:
        sine_wave_continuous = amplitude * np.sin(2 * np.pi * frequency * t_continuous + phase_shift)
        ax1.plot(t_continuous, sine_wave_continuous, label='Sine Wave (Continuous)', color='b')

# continous functions
    if plot_cosine:
        cosine_wave_continuous = amplitude * np.cos(2 * np.pi * frequency * t_continuous + phase_shift)
        ax1.plot(t_continuous, cosine_wave_continuous, label='Cosine Wave (Continuous)', color='r')

    ax1.set_title("Continuous Signal", fontsize=16, color='black')
    ax1.set_xlabel("Time (s)", fontsize=14, color='black')
    ax1.set_ylabel("Amplitude", fontsize=14, color='black')
    ax1.grid(True, color='gray')
    ax1.legend(loc='lower left', fontsize=12, facecolor='white', edgecolor='black')
    ax1.set_facecolor("white")

# discrete functions
    if plot_sine:
        sine_wave_discrete = amplitude * np.sin(2 * np.pi * frequency * t_discrete + phase_shift)
        ax2.stem(t_discrete, sine_wave_discrete, label='Sine Wave (Discrete)', linefmt='b-', markerfmt='bo',
                 basefmt='k-')
        ax2.plot(t_discrete, sine_wave_discrete, color='b', alpha=0.5)

    if plot_cosine:
        cosine_wave_discrete = amplitude * np.cos(2 * np.pi * frequency * t_discrete + phase_shift)
        ax2.stem(t_discrete, cosine_wave_discrete, label='Cosine Wave (Discrete)', linefmt='r-', markerfmt='ro',
                 basefmt='k-')
        ax2.plot(t_discrete, cosine_wave_discrete, color='r', alpha=0.5)

    ax2.set_title("Discrete Signal", fontsize=16, color='black')
    ax2.set_xlabel("Time (s)", fontsize=14, color='black')
    ax2.set_ylabel("Amplitude", fontsize=14, color='black')
    ax2.grid(True, color='gray')
    ax2.legend(loc='lower left', fontsize=12, facecolor='white', edgecolor='black')
    ax2.set_facecolor("white")

    fig.patch.set_facecolor("white")
    plt.tight_layout()
    plt.show()


def open_task2():
    task2_window = tk.Toplevel()
    task2_window.geometry("400x500")
    task2_window.title("Task 2 - Sine/Cosine Signal Plotter")
    task2_window.configure(bg=BG_COLOR)

    amplitude = tk.DoubleVar()
    frequency = tk.DoubleVar()
    duration = tk.DoubleVar()
    phase_shift = tk.DoubleVar()
    sampling_frequency = tk.DoubleVar()
    sine_var = tk.BooleanVar(value=False)
    cosine_var = tk.BooleanVar(value=False)

    tk.Label(task2_window, text="Amplitude:", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)
    tk.Entry(task2_window, textvariable=amplitude, bg=ENTRY_BG, fg=ENTRY_FG, font=FONT).pack(pady=5)

    tk.Label(task2_window, text="Frequency (Hz):", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)
    tk.Entry(task2_window, textvariable=frequency, bg=ENTRY_BG, fg=ENTRY_FG, font=FONT).pack(pady=5)

    tk.Label(task2_window, text="Sampling Frequency (Hz):", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)
    tk.Entry(task2_window, textvariable=sampling_frequency, bg=ENTRY_BG, fg=ENTRY_FG, font=FONT).pack(pady=5)

    tk.Label(task2_window, text="Duration (seconds):", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)
    tk.Entry(task2_window, textvariable=duration, bg=ENTRY_BG, fg=ENTRY_FG, font=FONT).pack(pady=5)

    tk.Label(task2_window, text="Phase Shift (radians):", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)
    tk.Entry(task2_window, textvariable=phase_shift, bg=ENTRY_BG, fg=ENTRY_FG, font=FONT).pack(pady=5)

    tk.Checkbutton(task2_window, text="Sine", variable=sine_var, bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)
    tk.Checkbutton(task2_window, text="Cosine", variable=cosine_var, bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=5)

    tk.Button(task2_window, text="Generate Signal",
              command=lambda: plot_signals(amplitude.get(), frequency.get(), duration.get(), phase_shift.get(),
                                           sampling_frequency.get(), sine_var.get(), cosine_var.get()),
              bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=20)

    tk.Button(task2_window, text="Back to Main Menu", command=task2_window.destroy, bg=BTN_BG, fg=BTN_FG,
              font=FONT).pack(pady=20)





#Task 3 Functions

def quantize_signal1(signal, levels=None):
    indices, samples = signal


    # Calculate min, max, and delta for quantization range
    min_val, max_val = min(samples), max(samples)
    delta = (max_val - min_val) / levels

    # Create ranges for quantization
    ranges = [min_val + i * delta for i in range(levels + 1)]
    quantize_samples = []
    encoded_samples = []

    # Quantize samples and compute encoding
    for sample in samples:
        for j in range(1, len(ranges)):
            # Adjusted condition to include edge cases
            if sample <= ranges[j] or (j == len(ranges) - 1):
                quantized_value = round((ranges[j] + ranges[j-1]) / 2, 2)
                quantize_samples.append(quantized_value)

                # Binary encoding for quantization level
                encoded_value = f"{j-1:03b}"  # 3-bit binary encoding
                encoded_samples.append(encoded_value)
                break
    
    # Calculate quantization error
    quantization_error = [original - quantized for original, quantized in zip(samples, quantize_samples)]
    
    # Plot function call remains the same
    plot_quantized_signal(indices, samples, quantize_samples, quantization_error, encoded_samples)
    return quantize_samples, quantization_error, encoded_samples

def quantize_signal2(signal, levels=None, bits=None):
    indices, samples = signal

    # Set levels based on bits if provided, otherwise default to 256 levels
    if levels is None and bits is not None:
        levels = 2 ** bits
    elif levels is None:
        levels = 256  

    # Calculate min, max, and delta for quantization range
    min_val, max_val = min(samples), max(samples)
    delta = (max_val - min_val) / levels

    # Create ranges for quantization
    ranges = [min_val + i * delta for i in range(levels + 1)]
    quantize_samples = []
    encoded_samples = []
    intervals = []

    # Quantize samples and compute encoding
    for sample in samples:
        for j in range(1, len(ranges)):
            # Adjusted condition to include edge cases
            if sample <= ranges[j] or (j == len(ranges) - 1):
                quantized_value = round((ranges[j] + ranges[j-1]) / 2, 3)
                quantize_samples.append(quantized_value)

                # Binary encoding for quantization level
                encoded_value = f"{j-1:02b}"  # 2-bit binary encoding
                encoded_samples.append(encoded_value)
                intervals.append(j)
                break
    
    # Calculate quantization error
    quantization_error = [round(quantized - original,3) for original, quantized in zip(samples, quantize_samples)]
    
    # Plot function call remains the same
    plot_quantized_signal(indices, samples, quantize_samples, quantization_error, encoded_samples)
    return quantize_samples, quantization_error, encoded_samples,intervals




def plot_quantized_signal(indices, original_samples, quantized_samples, quantization_error, encoded_samples):
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(indices, original_samples, marker='o', linestyle='-', color='b', label="Original Signal")
    plt.plot(indices, quantized_samples, marker='x', linestyle='-', color='r', label="Quantized Signal")
    plt.title("Original vs Quantized Signal", fontsize=16, color='black')
    plt.xlabel('Index', fontsize=14, color='black')
    plt.ylabel('Amplitude', fontsize=14, color='black')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(indices, quantization_error, marker='o', linestyle='-', color='purple', label="Quantization Error")
    plt.title("Quantization Error", fontsize=16, color='black')
    plt.xlabel('Index', fontsize=14, color='black')
    plt.ylabel('Error', fontsize=14, color='black')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.stem(indices, encoded_samples, linefmt='g-', markerfmt='go', basefmt='k-', label="Encoded Signal (Binary)")
    plt.title("Encoded Signal (Binary Levels)", fontsize=16, color='black')
    plt.xlabel('Index', fontsize=14, color='black')
    plt.ylabel('Encoded Level', fontsize=14, color='black')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def perform_quantization():
    if Signal3:
        bits = simpledialog.askinteger("Quantization Bits", "Enter the number of bits:", minvalue=1)
        levels = 2 ** bits if bits is not None else None
        quantized_samples, quantization_error, encoded_samples = quantize_signal1(Signal3, levels=levels)
        QuanTest1.QuantizationTest1("Quan1_Out.txt", encoded_samples, quantized_samples)
        quantized_samples2, quantization_error2, encoded_samples2,intervals = quantize_signal2(Signal3, levels=levels)
        QuanTest2.QuantizationTest2("Quan2_Out.txt",intervals,encoded_samples2,quantized_samples2,quantization_error2)
        print("Quantized Samples:", quantized_samples2)
        print("Quantization Error:", quantization_error2)
        print("Encoded Signal (Binary Levels):", encoded_samples2)
        print("intervals = ",intervals)
    else:
        messagebox.showwarning("Error", "Please load Signal 3!")



def load_signal3():
    global Signal3
    file_path = filedialog.askopenfilename(title="Select Signal 3 File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        Signal3 = ReadSignalFile(file_path)
        messagebox.showinfo("Success", "Signal 3 Loaded Successfully!")


# def perform_quantization():
#     if Signal3:
#         levels = simpledialog.askinteger("Quantization Levels", "Enter the number of quantization levels (leave blank for bits):", minvalue=1)
#         bits = None
#         if levels is None:
#             bits = simpledialog.askinteger("Quantization Bits", "Enter the number of bits:", minvalue=1)
#         quantized_samples, quantization_error, encoded_samples = quantize_signal(Signal3, levels=levels, bits=bits)
#         QuanTest1.QuantizationTest1("Quan1_Out.txt",encoded_samples,quantized_samples)
#         print("Quantized Samples:", quantized_samples)
#         print("Quantization Error:", quantization_error)
#         print("Encoded Signal (Levels):", encoded_samples)
#     else:
#         messagebox.showwarning("Error", "Please load Signal 3!")


### Task 3 GUI ###

def open_task3():
    task3_window = tk.Toplevel()
    task3_window.geometry("400x300")
    task3_window.title("Task 3 - Quantization")
    task3_window.configure(bg=BG_COLOR)

    tk.Button(task3_window, text="Load Signal 3", command=load_signal3, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=10)
    tk.Button(task3_window, text="Perform Quantization", command=perform_quantization, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=10)

    tk.Button(task3_window, text="Back to Main Menu", command=task3_window.destroy, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=20)















### Main Menu ###

def main_menu():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Main Menu")
    root.configure(bg=BG_COLOR)

    tk.Label(root, text="Select a Task", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 18, "bold")).pack(pady=20)

    tk.Button(root, text="Task 1: Signal Operations", command=open_task1, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=10)
    tk.Button(root, text="Task 2: Plot Sine/Cosine Signal", command=open_task2, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=10)
    tk.Button(root, text="Task 3: Quantization", command=open_task3, bg=BTN_BG, fg=BTN_FG, font=FONT).pack(pady=10)

    root.mainloop()


### Run the Main Menu ###
main_menu()
