import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

from tkinter import filedialog, Tk, Button, simpledialog, messagebox, Entry, Label
from main_task_2 import *
class SignalProcessingApp_task_2:
    def __init__(self, master):
        self.master = master
        # master.title("Task 2")
        # master.geometry("350x350")

        self.signals = []
        self.current_result = None  # Store the result for saving


        self.sin_button = Button(master, text="sin signal", command=self.sin_signal)
        self.sin_button.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')

        self.sin_input_A = Entry(master)
        self.sin_input_A.grid(row=6, column=1, padx=5, pady=5, sticky='nsew')
        self.sin_input_A.insert(0, "Enter Amplitude value")
        self.sin_input_A.bind("<FocusIn>", self.clear_placeholder)
        self.sin_input_A.bind("<FocusOut>", self.set_placeholder)

        self.sin_input_theta = Entry(master)
        self.sin_input_theta.grid(row=7, column=1, padx=5, pady=5, sticky='nsew')
        self.sin_input_theta.insert(0, "Enter Theta value")
        self.sin_input_theta.bind("<FocusIn>", self.clear_placeholder)
        self.sin_input_theta.bind("<FocusOut>", self.set_placeholder)

        self.sin_input_analog_freq = Entry(master)
        self.sin_input_analog_freq.grid(row=8, column=1, padx=5, pady=5, sticky='nsew')
        self.sin_input_analog_freq.insert(0, "Enter Analog freq")
        self.sin_input_analog_freq.bind("<FocusIn>", self.clear_placeholder)
        self.sin_input_analog_freq.bind("<FocusOut>", self.set_placeholder)

        self.sin_input_sampling_freq = Entry(master)
        self.sin_input_sampling_freq.grid(row=9, column=1, padx=5, pady=5, sticky='nsew')
        self.sin_input_sampling_freq.insert(0, "Enter Sampling freq")
        self.sin_input_sampling_freq.bind("<FocusIn>", self.clear_placeholder)
        self.sin_input_sampling_freq.bind("<FocusOut>", self.set_placeholder)

        self.sin_input_duration = Entry(master)
        self.sin_input_duration.grid(row=10, column=1, padx=5, pady=5, sticky='nsew')
        self.sin_input_duration.insert(0, "Enter Duration")
        self.sin_input_duration.bind("<FocusIn>", self.clear_placeholder)
        self.sin_input_duration.bind("<FocusOut>", self.set_placeholder)

        self.cos_button = Button(master, text="cos signal", command=self.cos_signal)
        self.cos_button.grid(row=11, column=0, padx=5, pady=5, sticky='nsew')

        self.cos_input_A = Entry(master)
        self.cos_input_A.grid(row=11, column=1, padx=5, pady=5, sticky='nsew')
        self.cos_input_A.insert(0, "Enter Amplitude value")
        self.cos_input_A.bind("<FocusIn>", self.clear_placeholder)
        self.cos_input_A.bind("<FocusOut>", self.set_placeholder)

        self.cos_input_theta = Entry(master)
        self.cos_input_theta.grid(row=12, column=1, padx=5, pady=5, sticky='nsew')
        self.cos_input_theta.insert(0, "Enter Theta value")
        self.cos_input_theta.bind("<FocusIn>", self.clear_placeholder)
        self.cos_input_theta.bind("<FocusOut>", self.set_placeholder)

        self.cos_input_analog_freq = Entry(master)
        self.cos_input_analog_freq.grid(row=13, column=1, padx=5, pady=5, sticky='nsew')
        self.cos_input_analog_freq.insert(0, "Enter Analog freq")
        self.cos_input_analog_freq.bind("<FocusIn>", self.clear_placeholder)
        self.cos_input_analog_freq.bind("<FocusOut>", self.set_placeholder)

        self.cos_input_sampling_freq = Entry(master)
        self.cos_input_sampling_freq.grid(row=14, column=1, padx=5, pady=5, sticky='nsew')
        self.cos_input_sampling_freq.insert(0, "Enter Sampling freq")
        self.cos_input_sampling_freq.bind("<FocusIn>", self.clear_placeholder)
        self.cos_input_sampling_freq.bind("<FocusOut>", self.set_placeholder)

        self.cos_input_duration = Entry(master)
        self.cos_input_duration.grid(row=15, column=1, padx=5, pady=5, sticky='nsew')
        self.cos_input_duration.insert(0, "Enter Duration")
        self.cos_input_duration.bind("<FocusIn>", self.clear_placeholder)
        self.cos_input_duration.bind("<FocusOut>", self.set_placeholder)

    # Methods to handle placeholder behavior
    def clear_placeholder(self, event):
        if event.widget.get() in ["Enter Amplitude value", "Enter Theta value","Enter Analog freq","Enter Sampling freq","Enter Duration"]:
            event.widget.delete(0, 'end')

    def set_placeholder(self, event):
        if event.widget.get() == "":
            if event.widget == self.input_multiply_val:
                event.widget.insert(0, "Enter Amplitude value")
            elif event.widget == self.input_shift_val:
                event.widget.insert(0, "Enter Theta value")
            elif event.widget == self.input_shift_val:
                event.widget.insert(0, "Enter Analog freq")
            elif event.widget == self.input_shift_val:
                event.widget.insert(0, "Enter Sampling freq")
            elif event.widget == self.input_shift_val:
                event.widget.insert(0, "Enter Duration")

    def sin_signal(self):
        A = float(self.sin_input_A.get())
        theta = float(self.sin_input_theta.get())
        analog_freq = float(self.sin_input_analog_freq.get())
        sampling_freq = float(self.sin_input_sampling_freq.get())
        duration = float(self.sin_input_duration.get())
        if sampling_freq<2*analog_freq:
            messagebox.showwarning("Error", "there is aliasing")
            return
        
        t_Discrete, sine_wave__Discrete = generate_sine_wave(A,theta,analog_freq,sampling_freq,duration)
        t_Continuous, sine_wave__Continuous = generate_sine_wave(A,theta,analog_freq,1000,duration)
        self.current_result = (t_Discrete, sine_wave__Discrete,t_Continuous,sine_wave__Continuous,)  # Store result for saving
        display_signal(t_Discrete, sine_wave__Discrete,t_Continuous,sine_wave__Continuous, title="Sine")

    def cos_signal(self):
        A = float(self.cos_input_A.get())
        theta = float(self.cos_input_theta.get())
        analog_freq = float(self.cos_input_analog_freq.get())
        sampling_freq = float(self.cos_input_sampling_freq.get())
        duration = float(self.cos_input_duration.get())
        if sampling_freq<2*analog_freq:
            messagebox.showwarning("Error", "there is aliasing")
            return
        t_Discrete, cosine_wave__Discrete = generate_cosine_wave(A,theta,analog_freq,sampling_freq,duration)
        t_Continuous, cosine_wave__Continuous = generate_cosine_wave(A,theta,analog_freq,1000,duration)
        self.current_result = (t_Discrete, cosine_wave__Discrete,t_Continuous,cosine_wave__Continuous,)  # Store result for saving
        display_signal(t_Discrete, cosine_wave__Discrete,t_Continuous,cosine_wave__Continuous, title="Cosine")
