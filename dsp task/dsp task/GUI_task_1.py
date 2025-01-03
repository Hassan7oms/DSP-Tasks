import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

from tkinter import filedialog, Tk, Button, simpledialog, messagebox, Entry, Label
from main_task_1 import *
from DSP_Task_2_TEST_functions import *
class SignalProcessingApp_task_1:
    def __init__(self, master):
        self.master = master
        # master.title("Task 1")
        # master.geometry("300x250")

        self.signals = []
        self.current_result = None  # Store the result for saving

        self.load_button = Button(master, text="Load Signal", command=self.load_signal)
        self.load_button.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.add_button = Button(master, text="Add Signals", command=self.add_signals)
        self.add_button.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.subtract_button = Button(master, text="Subtract Signals", command=self.subtract_signals)
        self.subtract_button.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        self.multiply_button = Button(master, text="Multiply Signal", command=self.multiply_signal)
        self.multiply_button.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

        self.multiply_input = Entry(master)
        self.multiply_input.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
        self.multiply_input.insert(0, "Enter multiply value")
        self.multiply_input.bind("<FocusIn>", self.clear_placeholder)
        self.multiply_input.bind("<FocusOut>", self.set_placeholder)

        self.shift_button = Button(master, text="Shift Signal", command=self.shift_signal)
        self.shift_button.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')
        
        self.shift_input = Entry(master)
        self.shift_input.grid(row=4, column=1, padx=5, pady=5, sticky='nsew')
        self.shift_input.insert(0, "Enter shift value")
        self.shift_input.bind("<FocusIn>", self.clear_placeholder)
        self.shift_input.bind("<FocusOut>", self.set_placeholder)

        self.reverse_button = Button(master, text="Reverse Signal", command=self.reverse_signal)
        self.reverse_button.grid(row=5, column=0, padx=5, pady=5, sticky='nsew')


    # Methods to handle placeholder behavior
    def clear_placeholder(self, event):
        if event.widget.get() in ["Enter multiply value", "Enter shift value"]:
            event.widget.delete(0, 'end')

    def set_placeholder(self, event):
        if event.widget.get() == "":
            if event.widget == self.input_multiply_val:
                event.widget.insert(0, "Enter multiply value")
            elif event.widget == self.input_shift_val:
                event.widget.insert(0, "Enter shift value")


    def load_signal(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return  # User canceled the file dialog
        indices, values = read_signal(file_path)
        self.signals.append((indices, values))
        display_signal(indices, values, title="Loaded Signal")

    def add_signals(self):
        if len(self.signals) < 2:
            messagebox.showwarning("Error", "You need to load at least two signals to add.")
            return
        indices, result = add_signals(self.signals)
        self.current_result = (indices, result)  # Store result for saving
        AddSignalSamplesAreEqual("Signal1.txt", "Signal2.txt",indices,result)
        display_signal(indices, result, title="Added Signals")

    def subtract_signals(self):
        if len(self.signals) < 2:
            messagebox.showwarning("Error", "You need to load at least two signals to subtract.")
            return
        indices1, values1 = self.signals[0]
        indices2, values2 = self.signals[1]

        # Multiply the second signal by -1
        neg_values2 = values2 * -1

        # Now add the first signal with the negated second signal
        indices, result = add_signals([(indices1, values1), (indices2, neg_values2)])
        self.current_result = (indices, result)  # Store result for saving
        SubSignalSamplesAreEqual("Signal1.txt", "Signal2.txt",indices,result)
        display_signal(indices, result, title="Subtracted Signals")

    def multiply_signal(self):
        if not self.signals:
            messagebox.showwarning("Error", "You need to load a signal first.")
            return
        constant = float(self.multiply_input.get())
        if constant is None:
            return  # User canceled the input dialog
        indices, values = self.signals[0]
        indices, result = apply_multiplication(indices, values, constant)
        self.current_result = (indices, result)  # Store result for saving
        MultiplySignalByConst(constant,indices, result)#constant = 5
        display_signal(indices, result, title="Multiplied Signal")

    def shift_signal(self):
        if not self.signals:
            messagebox.showwarning("Error", "You need to load a signal first.")
            return
        k = float(self.shift_input.get())
        if k is None:
            return  # User canceled the input dialog
        indices, values = self.signals[0]
        indices, result = apply_shift(indices, values, k)
        self.current_result = (indices, result)  # Store result for saving
        ShiftSignalByConst(k,indices,result)#k = 3 or k = -3
        display_signal(indices, result, title="Shifted Signal")

    def reverse_signal(self):
        if not self.signals:
            messagebox.showwarning("Error", "You need to load a signal first.")
            return
        indices, values = self.signals[0]
        indices, result = apply_reverse(indices, values)
        self.current_result = (indices, result)  # Store result for saving
        Folding(indices,result)
        display_signal(indices, result, title="Reversed Signal")
