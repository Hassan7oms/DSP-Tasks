import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog, Button, messagebox, Entry, Label, StringVar, Radiobutton
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, Tk, Button, simpledialog, messagebox, Entry, Label
from tkinter import *
from main_task_6 import *

class SignalProcessingApp_task_6:
    def __init__(self, master):
        self.master = master
        self.signals = []
        self.folders = []
        self.current_result = None

        # Existing elements
        self.load_signal_button = Button(master, text="Load Signals", command=self.load_signal)
        self.load_signal_button.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        # Perform Convolution Button
        self.convolution_button = Button(master, text="Perform Convolution", command=self.perform_convolution)
        self.convolution_button.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        #compare
        self.compare_button = Button(master, text="Compare Signals", command=self.compare_signals)
        self.compare_button.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

        # Perform delay Button
        self.delay_button = Button(master, text="calculate delay", command=self.perform_delay)
        self.delay_button.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')

        self.load_test_button = Button(master, text="Load test", command=self.load_test)
        self.load_test_button.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')

        #read folders
        self.load_folders_button = Button(master, text="Load folders", command=self.load_folders)
        self.load_folders_button.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')

         #read classify
        self.classify_button = Button(master, text="Classify", command=self.perform_Classify)
        self.classify_button.grid(row=7, column=0, padx=5, pady=5, sticky='nsew')

        # New input for window size
        self.clear_button = Button(master, text="Clear Signals", command=self.clear_signals)
        self.clear_button.grid(row=8, column=0, padx=5, pady=5, sticky='nsew')

    
    def clear_placeholder(self, event):
        if self.window_size_input.get() == "Enter window size":
            self.window_size_input.delete(0, "end")

    def set_placeholder(self, event):
        if not self.window_size_input.get():
            self.window_size_input.insert(0, "Enter window size")

    def load_signal(self):
        """Load the first signal."""
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        indices, values = read_signal(file_path)
        
        self.signals.append((indices, values))
        messagebox.showinfo(f"Signal {len(self.signals)} Loaded", f"Signal {len(self.signals)} has been successfully loaded!")
        PlotSignal(self.signals[len(self.signals)-1], title=f"Singal {len(self.signals)}")
    

    def perform_convolution(self):
        """Perform convolution of the two loaded signals."""
        if len(self.signals) < 2:
            messagebox.showwarning("Error", "Please load two signals first!")
            return
        delay_samples,bst_corr,result_indices,result_amplitudes=Convolotion(self.signals[0], self.signals[1])
        self.current_result=(result_indices, result_amplitudes)
        PlotSignal(self.current_result, title=f"Convoluted Siganl")

    def compare_signals(self):
        """Compare two signals."""
        if not self.current_result:
            messagebox.showwarning("Error", "Please load both signals to compare!")
            return
        file_path = filedialog.askopenfilename()
        for i,j in zip(self.current_result[0],self.current_result[1]):
            print(i," ",j)
        Compare_Signals(file_path,self.current_result[0], self.current_result[1])

    def perform_delay(self):
        """Perform convolution of the two loaded signals."""
        if len(self.signals) < 2:
            messagebox.showwarning("Error", "Please load two signals first!")
            return
        delay_samples,bst_corr,result_indices,result_amplitudes=Convolotion(self.signals[0], self.signals[1])
        print(delay_samples)
        print(delay_samples/100)

    def load_test(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        indices, values = read_test(file_path)
        
        self.signals.append((indices, values))
        messagebox.showinfo(f"Signal {len(self.signals)} Loaded", f"Signal {len(self.signals)} has been successfully loaded!")
        PlotSignal(self.signals[len(self.signals)-1], title=f"Singal {len(self.signals)}")

    def load_folders(self):
        signal = read_folder()
        self.folders.append(signal)
        messagebox.showinfo(f"folder {len(self.folders)} Loaded", f"Signal {len(self.folders)} has been successfully loaded!")

    def perform_Classify(self):
        A,B = classify(self.signals[0],self.folders)
        if A>=B :
            print("down")
        else :
            print("up")

    def clear_signals(self):
        """Clear the signals list and reset attributes."""
        self.signals = []
        self.current_result = None
        
        self.tests= []
        messagebox.showinfo("Cleared", "All signals and results have been cleared.")