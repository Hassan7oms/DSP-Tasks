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
from main_task_5 import *
from QuanTest1 import *
from main_task_4 import *

class SignalProcessingApp_task_5:
    def __init__(self, master):
        self.master = master
        self.signals = []
        self.current_result = None
        self.amp = None
        self.phase = None
        self.placeholder_text = "Enter frequency"

        # Load Signal Button
        self.load_button = Button(master, text="Load Signal", command=self.load_signal)
        self.load_button.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.freq_input = Entry(master)
        self.freq_input.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.freq_input.insert(0, self.placeholder_text)
        self.freq_input.bind("<FocusIn>", self.clear_placeholder)
        self.freq_input.bind("<FocusOut>", self.set_placeholder)

        # Apply DFT Button
        self.dft_button = Button(master, text="Apply DFT", command=self.apply_dft)
        self.dft_button.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

        # Apply IDFT Button
        self.idft_button = Button(master, text="Apply IDFT", command=self.apply_idft)
        self.idft_button.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')

    def load_signal(self):
        """Load a signal from a file."""
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        indices, values = read_signal(file_path)
        self.signals = (indices, values)  # Store as a tuple
        messagebox.showinfo("Signal Loaded", "Signal has been successfully loaded!")

    def apply_dft(self):
        """Apply the Discrete Fourier Transform (DFT)."""
        if not self.signals:
            messagebox.showerror("Error", "No signal loaded.")
            return

        try:
            sampling_freq = float(self.freq_input.get())  # Convert input to float
            self.current_result, self.amp, self.phase = apply_DFT(sampling_freq, self.signals)
            messagebox.showinfo("DFT Completed", "DFT has been successfully applied!")
        except ValueError:
            messagebox.showerror("Error", "Invalid frequency input. Please enter a numeric value.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply DFT: {e}")

    def apply_idft(self):
        """Apply the Inverse Discrete Fourier Transform (IDFT)."""
        if self.amp is None or self.phase is None:
            messagebox.showerror("Error", "No DFT data available. Apply DFT first.")
            return

        try:
            indecis,values = apply_IDFT(self.current_result)
            PlotSignal(indecis,values, title="Reconstructed Signal (IDFT)")
            messagebox.showinfo("IDFT Completed", "IDFT has been successfully applied!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply IDFT: {e}")


    def clear_placeholder(self, event):
        if self.freq_input.get() == "Enter frequency":
            self.freq_input.delete(0, "end")


    def set_placeholder(self, event):
        if not self.freq_input.get():
            self.freq_input.insert(0, "Enter frequency")

