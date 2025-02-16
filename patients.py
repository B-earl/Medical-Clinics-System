# patients.py
import tkinter as tk
from tkinter import messagebox
from utils import display_table
from data import patients  # Import shared patients array

def open_patients():
    # Create new window for patients
    patients_window = tk.Toplevel()
    patients_window.title("Patients")
    patients_window.geometry("600x400")

    # Create a frame for displaying the table of appointments (patients)
    table_frame = tk.Frame(patients_window)
    table_frame.pack(pady=10)

    # Display table with headers and data
    headers = ["Patient Name", "Doctor Name", "Date", "Time", "Symptoms"]  # Include Symptoms in the headers
    display_table(table_frame, patients, headers)

    patients_window.mainloop()
