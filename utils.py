# utils.py
import tkinter as tk

# Function to display data in a table
def display_table(frame, data, headers):
    # Clear previous content
    for widget in frame.winfo_children():
        widget.grid_forget()

    # Table headers
    for col, header in enumerate(headers):
        tk.Label(frame, text=header, font=('Arial', 10, 'bold')).grid(row=0, column=col, padx=5, pady=5)

    # Populate the table with data
    for i, record in enumerate(data):
        row = i + 1
        for j, key in enumerate(record):
            tk.Label(frame, text=record[key]).grid(row=row, column=j, padx=5, pady=5)
