import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog, Button, messagebox, Entry, Label, StringVar, Radiobutton
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, Tk, Button, simpledialog, messagebox, Entry, Label
from tkinter import *
from main_task_7 import *
from main_task_5 import *
from main_task_4 import *
from types import SimpleNamespace
from CompareSignal import *
from main_task_1 import *
class SignalProcessingApp_task_7:
    def __init__(self, master):
        self.master = master
        self.signals = []
        self.folders = []
        self.config = SimpleNamespace
        self.current_result_convlution = None
        self.current_result = None
        self.current_result_fast_indices = None
        self.current_result_fast_values = None
        # Existing elements
        self.load_specifications_button = Button(master, text="Load Specifications", command=self.load_specifications)
        self.load_specifications_button.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.create_filter_button = Button(master, text="Create Filter", command=self.create_filter)
        self.create_filter_button.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.compare_button = Button(master, text="Compare", command=self.Compare)
        self.compare_button.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        self.load_signall = Button(master, text="load signal", command=self.load_signal)
        self.load_signall.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

        self.direct_filter = Button(master, text="direct (conv)", command=self.perform_convolution)
        self.direct_filter.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')

        self.compare_conv_button = Button(master, text="Compare convlution", command=self.Compare_conv)
        self.compare_conv_button.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')

        self.fast_filter = Button(master, text="fast filter", command=self.perform_fast)
        self.fast_filter.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')
        
        self.compare_fast_button = Button(master, text="Compare fast", command=self.Compare_fast)
        self.compare_fast_button.grid(row=7, column=0, padx=5, pady=5, sticky='nsew')

    def load_signal(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return  # User canceled the file dialog
        indices, values = read_signal(file_path)
        self.signals.append((indices, values))
        display_signal(indices, values, title="Loaded Signal")

    def clear_placeholder(self, event):
        if self.window_size_input.get() == "Enter window size":
            self.window_size_input.delete(0, "end")

    def set_placeholder(self, event):
        if not self.window_size_input.get():
            self.window_size_input.insert(0, "Enter window size")
    
    def load_specifications(self):
        """Load the first signal."""

        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        self.config = read_specifications(file_path)
        print(vars(self.config))
        messagebox.showinfo(f"file specifications Loaded", f"file specifications has been successfully loaded!")

    def create_filter(self):
        self.current_result = get_filter(self.config)
        print(self.current_result[0][0]," ",self.current_result[1][0])
        messagebox.showinfo(f"file specifications Loaded", f"file specifications has been successfully loaded!")

    def Compare(self):
        """Compare two signals."""
        if not self.current_result:
            messagebox.showwarning("Error", "Please load signal to compare!")
            return
        file_path = filedialog.askopenfilename()
        for i,j in zip(self.current_result[0],self.current_result[1]):
            print(i," ",j)
        Compare_Signals(file_path,self.current_result[0], self.current_result[1])
    


###############################################################################################



    def perform_fast(self):
        """Apply the Discrete Fourier Transform (DFT)."""
        if not self.signals:
            messagebox.showerror("Error", "No signal loaded.")
            return
        def equalize_length_truncate(list1, list2):
            min_length = min(len(list1), len(list2))
            list1 = list1[:min_length]  # Truncate list1
            list2 = list2[:min_length]  # Truncate list2
            return list1, list2


        filter_padded, padded_signal = equalize_length_truncate(self.current_result, self.signals[0])
        # Zero-pad the filter to match the signal length
        
        try:
            sampling_freq = float(1)  # Convert input to float
            self.current_result__DFT_filter, self.amp_filter, self.phase_filter = apply_DFT(sampling_freq, self.current_result)
            messagebox.showinfo("DFT Completed", "DFT has been successfully applied in filter!")
        except ValueError:
            messagebox.showerror("Error", "Invalid frequency input. Please enter a numeric value.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply DFT in filter: {e}")
        try:
            sampling_freq = float(1)  # Convert input to float
            self.current_result_DFT_signal, self.amp_signal, self.phase_signal = apply_DFT(sampling_freq, self.signals[0])
            messagebox.showinfo("DFT Completed", "DFT has been successfully applied in signal!")
        except ValueError:
            messagebox.showerror("Error", "Invalid frequency input. Please enter a numeric value.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply DFT in signal: {e}")

        try:
            if self.current_result_DFT_signal is not None and self.current_result__DFT_filter is not None:
                result_multiplied = [a * b for a, b in zip(self.current_result_DFT_signal, self.current_result__DFT_filter)]
                self.current_result_fast_indices,self.current_result_fast_values = apply_IDFT(result_multiplied)
            else:
                messagebox.showerror("Error", "DFT results are not available for multiplication.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to multiply DFT results: {e}")

    def perform_convolution(self):
        """Perform convolution of the two loaded signals."""
        # if len(self.signals) < 2:
        #     messagebox.showwarning("Error", "Please load two signals first!")
        #     return
        self.current_result_convlution=Covolotion_Perform(self.signals[0], self.current_result)
        PlotSignal(self.current_result_convlution, title=f"Convoluted Siganl")

    def Compare_conv(self):
        """Compare two signals."""
        if not self.current_result:
            messagebox.showwarning("Error", "Please load signal to compare!")
            return
        file_path = filedialog.askopenfilename()
        for i,j in zip(self.current_result[0],self.current_result[1]):
            print(i," ",j)
        Compare_Signals(file_path,self.current_result_convlution[0], self.current_result_convlution[1])

    def Compare_fast(self):
        """Compare two signals."""
        if not self.current_result:
            messagebox.showwarning("Error", "Please load signal to compare!")
            return
        file_path = filedialog.askopenfilename()
        for i,j in zip(self.current_result_fast_indices,self.current_result_fast_values):
            print(i," ",j)
        Compare_Signals(file_path,self.current_result_fast_indices, self.current_result_fast_values)