from tkinter import *
class SignalProcessingApp:
    def __init__(self, master):
        self.master = master
        master.title("Signal Processing App")

        self.signals = []
        self.current_result = None  # Store the result for saving

        self.load_button = Button(master, text="Load Signal", command=self.load_signal)
        self.load_button.pack()

        self.add_button = Button(master, text="Add Signals", command=self.add_signals)
        self.add_button.pack()

        self.subtract_button = Button(master, text="Subtract Signals", command=self.subtract_signals)
        self.subtract_button.pack()

        self.multiply_button = Button(master, text="Multiply Signal by Constant", command=self.multiply_signal)
        self.multiply_button.pack()

        self.shift_button = Button(master, text="Shift Signal", command=self.shift_signal)
        self.shift_button.pack()

        self.reverse_button = Button(master, text="Reverse Signal", command=self.reverse_signal)
        self.reverse_button.pack()

        self.save_button = Button(master, text="Save Signal", command=self.save_signal)
        self.save_button.pack()
        self.view_sin=Button(master,text="continous",command=self.)

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
        display_signal(indices, result, title="Subtracted Signals")

    def multiply_signal(self):
        if not self.signals:
            messagebox.showwarning("Error", "You need to load a signal first.")
            return
        constant = simpledialog.askfloat("Input", "Enter a constant to multiply the signal:")
        if constant is None:
            return  # User canceled the input dialog
        indices, values = self.signals[0]
        indices, result = apply_multiplication(indices, values, constant)
        self.current_result = (indices, result)  # Store result for saving
        display_signal(indices, result, title="Multiplied Signal")

    def shift_signal(self):
        if not self.signals:
            messagebox.showwarning("Error", "You need to load a signal first.")
            return
        k = simpledialog.askinteger("Input", "Enter the number of steps to shift:")
        if k is None:
            return  # User canceled the input dialog
        indices, values = self.signals[0]
        indices, result = apply_shift(indices, values, k)
        self.current_result = (indices, result)  # Store result for saving
        display_signal(indices, result, title="Shifted Signal")

    def reverse_signal(self):
        if not self.signals:
            messagebox.showwarning("Error", "You need to load a signal first.")
            return
        indices, values = self.signals[0]
        indices, result = apply_reverse(indices, values)
        self.current_result = (indices, result)  # Store result for saving
        display_signal(indices, result, title="Reversed Signal")

    def save_signal(self):
        if self.current_result is None:
            messagebox.showwarning("Error", "No signal to save. Please process a signal first.")
            return
        indices, values = self.current_result
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return  # User canceled save dialog
        save_signal(indices, values, filename=file_path)

root = Tk()
root.geometry("800x500")
app = SignalProcessingApp(root)
root.mainloop()

