import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog, Button, messagebox, Entry, Label, StringVar, Radiobutton
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, Tk, Button, simpledialog, messagebox, Entry, Label
from tkinter import *
from main_task_3 import *
from main_task_1 import *
from QuanTest1 import *
from main_task_4 import *

class SignalProcessingApp_task_4:
    def __init__(self, master):
        self.master = master
        self.signals = []
        self.current_result = None
        self.tests= []

        # Existing elements
        self.load_button = Button(master, text="Load Signal", command=self.load_signal1)
        self.load_button.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.load_signal2_button = Button(master, text="Load test singal", command=self.load_signal2)
        self.load_signal2_button.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        # New input for window size
        self.clear_button = Button(master, text="Clear Signals", command=self.clear_signals)
        self.clear_button.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
        self.window_size_input = Entry(master)
        self.window_size_input.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        self.window_size_input.insert(0, "Enter window size")
        self.window_size_input.bind("<FocusIn>", self.clear_placeholder)
        self.window_size_input.bind("<FocusOut>", self.set_placeholder)

        # Button to compute moving average
        self.moving_avg_button = Button(master, text="Compute Moving Average", command=self.compute_moving_average)
        self.moving_avg_button.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')

        # Perform Convolution Button
        self.convolution_button = Button(master, text="Perform Convolution", command=self.perform_convolution)
        self.convolution_button.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')

        # Perform Derivative Button
        self.derivative_button = Button(master, text="Compute first Derivative", command=self.compute_derivative1)
        self.derivative_button.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')
        self.derivative_button = Button(master, text="Compute second Derivative", command=self.compute_derivative2)
        self.derivative_button.grid(row=6, column=1, padx=5, pady=5, sticky='nsew')

        self.compare_button = Button(master, text="Compare Signals", command=self.compare_signals)
        self.compare_button.grid(row=7, column=0, padx=5, pady=5, sticky='nsew')

        
    
    def compare_signals(self):
        """Compare two signals."""
        if not self.current_result or not self.tests[0]:
            messagebox.showwarning("Error", "Please load both signals to compare!")
            return
        CompareSignals(self.current_result, self.tests[0])

    def clear_placeholder(self, event):
        if self.window_size_input.get() == "Enter window size":
            self.window_size_input.delete(0, "end")

    def set_placeholder(self, event):
        if not self.window_size_input.get():
            self.window_size_input.insert(0, "Enter window size")

    def compute_moving_average(self):
        window_size = self.window_size_input.get()
        if not window_size.isdigit() or int(window_size) <= 0:
            messagebox.showwarning("Error", "Please enter a valid positive integer for window size.")
            return
        self.current_result=Moving_average_Perform(window_size,self.signals[0])
        PlotSignal(self.current_result, title=f"Moved average  Signal By {window_size}")

    def load_signal2(self):
        """Load the second signal."""
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        indices, values = read_signal(file_path)
        self.tests.append((indices, values))
        messagebox.showinfo("Signal 2 Loaded", "Signal 2 has been successfully loaded!")

    def load_signal1(self):
        """Load the first signal."""
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        indices, values = read_signal(file_path)
        
        self.signals.append((indices, values))
        messagebox.showinfo("Signal 1 Loaded", "Signal 1 has been successfully loaded!")
        PlotSignal(self.signals[0], title=f"Singal 1")
        if self.signals[1]:
           PlotSignal(self.signals[1], title=f"singal 2") 

    def perform_convolution(self):
        """Perform convolution of the two loaded signals."""
        if len(self.signals) < 2:
            messagebox.showwarning("Error", "Please load two signals first!")
            return
        self.current_result=Covolotion_Perform(self.signals[0], self.signals[1])
        PlotSignal(self.current_result, title=f"Convoluted Siganl")

    def compute_derivative1(self):
        """Compute the derivative of the loaded signal."""
        if not self.signals:
            messagebox.showwarning("Error", "Please load a signal first!")
            return
        self.current_result=Derivative_Perform1(self.signals[0])
        PlotSignal(self.current_result, title=f"first Derifted Siganl")
    
    def compute_derivative2(self):
        """Compute the derivative of the loaded signal."""
        if not self.signals:
            messagebox.showwarning("Error", "Please load a signal first!")
            return
        self.current_result=Derivative_Perform2(self.signals[0])
        PlotSignal(self.current_result, title=f"second Derifted Siganl")

    def clear_signals(self):
        """Clear the signals list and reset attributes."""
        self.signals = []
        self.current_result = None
        
        self.tests= []
        messagebox.showinfo("Cleared", "All signals and results have been cleared.")