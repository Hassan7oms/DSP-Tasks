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

class SignalProcessingApp_task_3:
    def __init__(self, master):
        self.master = master
        # master.title("Task 3")
        # master.geometry("350x350")
        self.signals = []
        self.current_result = None  # Store the result for saving

        self.load_button = Button(master, text="Load Signal", command=self.load_signal)
        self.load_button.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        
        self.Quantize = Button(master, text="test1", command=self.quantize_signal)
        self.Quantize.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')

        self.test2 = Button(master, text="test2", command=self.qtest2)
        self.test2.grid(row=7, column=0, padx=5, pady=5, sticky='nsew')
        # Radio button selection between Level and Bits
        self.selection = StringVar()
        self.selection.set("level")  # Default selection

        self.level_radio = Radiobutton(master, text="Quantization Level", variable=self.selection, value="level")
        self.level_radio.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')

        self.bits_radio = Radiobutton(master, text="Number of Bits", variable=self.selection, value="bits")
        self.bits_radio.grid(row=5, column=1, padx=5, pady=5, sticky='nsew')

        self.quantize_N_input = Entry(master)
        self.quantize_N_input.grid(row=6, column=1, padx=5, pady=5, sticky='nsew')
        self.quantize_N_input.insert(0, "Enter quantization level or num of bits")
        self.quantize_N_input.bind("<FocusIn>", self.clear_placeholder)
        self.quantize_N_input.bind("<FocusOut>", self.set_placeholder)
        # self.figure = Figure(figsize=(12,8), dpi=50)
        # self.canvas = FigureCanvasTkAgg(self.figure, master)
        # self.canvas.get_tk_widget().grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    def clear_placeholder(self, event):
        if event.widget.get() in ["Enter quantization level or num of bits"]:
            event.widget.delete(0, 'end')

    def set_placeholder(self, event):
        if event.widget.get() == "":
            if event.widget == self.input_multiply_val:
                event.widget.insert(0, "Enter quantization level or num of bits")    
    def load_signal(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return  # User canceled the file dialog
        indices, values = read_signal(file_path)
        self.signals.append((indices, values))
        display_signal(indices, values, title="Loaded Signal")

    def quantize_signal(self):
        # Ensure a signal is loaded
        if not self.signals:
            messagebox.showwarning("No Signal", "Please load a signal first.")
            return
        
        input_value = self.quantize_N_input.get()
        try:
            quantize_value = int(input_value)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return

        # Determine if using levels or bits based on radio button selection
        if self.selection.get() == "level":
            quantization_levels = quantize_value
        else:  # If selected "bits"
            quantization_levels = 2 ** quantize_value

        # Perform quantization
        indices, values = self.signals[-1]
        quantized_signal, quantization_error, encoded_values = perform_quantization(values, quantization_levels)
        QuantizationTest1(encoded_values, list(quantized_signal))
        #save_quantization_results(encoded, quantized_signal[1])
        # Display the result
        
        display_signal_q(indices, values, quantized_signal, quantization_error,encoded_values)
    
    def qtest2(self):
        # Ensure a signal is loaded
        if not self.signals:
            messagebox.showwarning("No Signal", "Please load a signal first.")
            return
        
        input_value = self.quantize_N_input.get()
        try:
            quantize_value = int(input_value)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return

        # Determine if using levels or bits based on radio button selection
        if self.selection.get() == "level":
            quantization_levels = quantize_value
        else:  # If selected "bits"
            quantization_levels = 2 ** quantize_value

        # Perform quantization
        indices, values = self.signals[-1]
        quantized_signal, quantization_error, encoded_values,intervals = quantize_signal2(values, quantization_levels)
        #QuantizationTest1(encoded_values, list(quantized_signal))
        #save_quantization_results(encoded, quantized_signal[1])
        # Display the result
        QuantizationTest2(intervals, encoded_values, quantized_signal,quantization_error)
        display_signal_q(indices, values, quantized_signal, quantization_error,encoded_values)

