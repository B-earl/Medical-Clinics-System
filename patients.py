import tkinter as tk
from tkinter import ttk, messagebox
from utils import display_table
from data import patients  

def open_patients():
    # Create new window for patients
    patients_window = tk.Toplevel()
    patients_window.title("Patients")
    patients_window.geometry("700x400")
    patients_window.configure(bg="#E8F0FE")  # Light blue background

    # Create a centered frame with a white background 
    frame = tk.Frame(patients_window, bg="white", padx=20, pady=20, relief="ridge", bd=2)
    frame.pack(expand=True, padx=20, pady=20)

    # Title label
    title_label = tk.Label(
        frame, text="Patient Records", font=("Arial", 18, "bold"), bg="white", fg="#333"
    )
    title_label.pack(pady=(0, 10))

    # Table Frame
    table_frame = tk.Frame(frame, bg="white")
    table_frame.pack()

    # Treeview Table with Scrollbar
    columns = ["Patient Name", "Doctor Name", "Date", "Time", "Symptoms"]
    
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    
    # scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # column headers
    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=120)

    # patient data into the table
    for patient in patients:
        tree.insert("", "end", values=patient)

    tree.pack()

    patients_window.mainloop()
