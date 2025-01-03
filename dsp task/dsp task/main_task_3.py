import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Button, simpledialog, messagebox
from main_task_1 import *
from QuanTest2 import *



# def perform_quantization(signal_values, quantization_levels):
#     # Example quantization implementation (to be replaced with actual logic)
#     quantized_values = []
#     encoded_values = []
#     for value in signal_values:
#         # Simple quantization logic for illustration purposes
#         quantized_value = round(value * quantization_levels) / quantization_levels
#         encoded_value = f"{int(quantized_value * quantization_levels)}"  # Example encoding
#         quantized_values.append(quantized_value)
#         encoded_values.append(encoded_value)
#     return encoded_values, quantized_values
def perform_quantization(signal, levels=None):
    samples = signal


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
    return quantize_samples, quantization_error, encoded_samples

def quantize_signal2(signal, levels=4, bits=None):
    samples = signal

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
    return quantize_samples, quantization_error, encoded_samples,intervals



def display_signal_q(indices, signal, quantized_signal, quantization_error,encoded):
    """
    Displays the original, quantized signal, and quantization error.
    """
    
    plt.figure(figsize=(12, 8))

    # Original and Quantized Signals
    plt.subplot(2, 1, 1)
    plt.plot(indices, signal, label="Original Signal")
    plt.step(indices, quantized_signal, label="Quantized Signal", where="mid", color="red")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.title("Original vs Quantized Signal")
    plt.legend()

    # Quantization Error
    plt.subplot(2, 1, 2)
    plt.plot(indices, quantization_error, label="Quantization Error", color="purple")
    plt.xlabel("Sample")
    plt.ylabel("Error")
    plt.title("Quantization Error")
    plt.legend()

    plt.tight_layout()
    plt.show()

# def display_signal_q(self, indices, original_values, quantized_signal, quantization_error):
#         # Clear previous plots
#         self.figure.clear()

#         # Plot original signal
#         ax1 = self.figure.add_subplot(211)
#         ax1.plot(indices, original_values, label='Original Signal', color='blue')
#         ax1.set_title("Original Signal")
#         ax1.set_xlabel("Time")
#         ax1.set_ylabel("Amplitude")
#         ax1.legend()

#         # Plot quantized signal
#         ax2 = self.figure.add_subplot(212)
#         ax2.plot(indices, quantized_signal, label='Quantized Signal', color='red')
#         ax2.set_title(f"Quantized Signal (Error: {quantization_error})")
#         ax2.set_xlabel("Time")
#         ax2.set_ylabel("Amplitude")
#         ax2.legend()

#         # Refresh the canvas to display the new plots
#         self.canvas.draw()


def save_quantization_results(encoded_values, quantized_values,file_path="C:\\Users\\IDEAPAD GAMING\\Desktop\\dsp task\\GUI\\New Text Document.txt"):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as f:
            # Write the header (optional)
            f.write("Encoded Values, Quantized Values\n")
            
            # Iterate over both lists and write to the file
            for encoded, quantized in zip(encoded_values, quantized_values):
                f.write(f"{encoded}, {quantized}\n")
        
        print(f"Results saved successfully to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")