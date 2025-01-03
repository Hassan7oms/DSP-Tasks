
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk
from GUI_task_1 import SignalProcessingApp_task_1
from GUI_task_2 import SignalProcessingApp_task_2
from GUI_task_3 import SignalProcessingApp_task_3
from GUI_task_4 import SignalProcessingApp_task_4
from GUI_task_5 import SignalProcessingApp_task_5
from GUI_task_6 import SignalProcessingApp_task_6
from GUI_task_7 import SignalProcessingApp_task_7
# Create the main window
root = tk.Tk()
root.title("Main Application")
root.geometry("600x500")

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Create frames for each task
task_1_frame = ttk.Frame(notebook)
task_2_frame = ttk.Frame(notebook)
task_3_frame = ttk.Frame(notebook)
task_4_frame = ttk.Frame(notebook)
task_5_frame = ttk.Frame(notebook)
task_6_frame = ttk.Frame(notebook)
task_7_frame = ttk.Frame(notebook)
# Add frames to the Notebook
notebook.add(task_1_frame, text="Task 1")
notebook.add(task_2_frame, text="Task 2")
notebook.add(task_3_frame, text="Task 3")
notebook.add(task_4_frame, text="Task 4")
notebook.add(task_5_frame, text="Task 5")
notebook.add(task_6_frame, text="Task 6")
notebook.add(task_7_frame, text="Task 7")
# Initialize each task's application
app_task_1 = SignalProcessingApp_task_1(task_1_frame)  # Initialize Task 1
app_task_2 = SignalProcessingApp_task_2(task_2_frame)  # Initialize Task 2
app_task_3 = SignalProcessingApp_task_3(task_3_frame)  # Initialize Task 3
app_task_4 = SignalProcessingApp_task_4(task_4_frame)  # Initialize Task 4
app_task_5 = SignalProcessingApp_task_5(task_5_frame)  # Initialize Task 4
app_task_6 = SignalProcessingApp_task_6(task_6_frame)  # Initialize Task 4
app_task_7 = SignalProcessingApp_task_7(task_7_frame)  # Initialize Task 4
root.mainloop()  # Start the main event loop

