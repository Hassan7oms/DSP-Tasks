import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Button, simpledialog, messagebox
from main_task_1 import *
from QuanTest2 import *

def Moving_average_Perform(window_size,Signal1):
    
    if Signal1:
        window_size = int(window_size)
        indices, amplitudes = Signal1
        result = [sum(amplitudes[i:i + window_size]) / window_size for i in range(len(amplitudes) - window_size + 1)]
        ResultSignal = (range(len(result)), result)
        
        Signal1=ResultSignal
        return ResultSignal

    else:
        messagebox.showwarning("Error", "Please load Signal 1!")



def Covolotion_Perform(signal1, signal2):
    indices1, amplitudes1 = signal1
    indices2, amplitudes2 = signal2
    start_index = int(indices1[0] + indices2[0])  # Convert to integer
    end_index = int(indices1[-1] + indices2[-1])  # Convert to integer
    result_indices = range(start_index, end_index + 1)
    result_amplitudes = []
    for n in result_indices:
        sum_value = 0
        for k in range(len(amplitudes1)):
            index_h = n - indices1[k]
            if index_h in indices2:
                idx_h = np.where(indices2 == index_h)[0][0]  # Find the index in numpy array
                sum_value += amplitudes1[k] * amplitudes2[idx_h]
        result_amplitudes.append(sum_value)

    ResultSignal = (result_indices, result_amplitudes)
    
    return ResultSignal



def Derivative_Perform2(Signal1):
    
    if Signal1:
        indices, amplitudes = Signal1
        result = [amplitudes[i + 1] - 2*amplitudes[i] + amplitudes[i - 1]    for i in range(1, len(amplitudes) - 1)]
        ResultSignal = (range(len(result)), result)
        Signal1 = ResultSignal
        return ResultSignal

def Derivative_Perform1(Signal1):
    
    if Signal1:
        indices, amplitudes = Signal1
        result = [amplitudes[i] - amplitudes[i - 1] for i in range(1, len(amplitudes))]
        ResultSignal = (range(len(result)), result)
        Signal1 = ResultSignal
        return ResultSignal

def CompareSignals(signal1,signal2):
    if signal1 and signal2:
        indices, samples = signal1
        exepected_indices,exepected_samples=signal2

      #  print(len(exepected_samples),len(samples))
        if (len(exepected_samples)!=len(samples)) and (len(exepected_indices)!=len(indices)):
            print("Addition Test case failed, your signal have different length from the expected one")
            return
        for i in range(len(indices)):
            if(indices[i]!=exepected_indices[i]):
                print("Addition Test case failed, your signal have different indicies from the expected one")
                return
        for i in range(len(exepected_samples)):
            if abs(samples[i] - exepected_samples[i]) < 0.01:
                continue
            else:
                print("Addition Test case failed, your signal have different values from the expected one")
                return
        print("Addition Test case passed successfully")
    else:
        messagebox.showwarning("Error", "Please Be Sure that you have uploaded the 2 signals!")

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