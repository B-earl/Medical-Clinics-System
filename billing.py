import tkinter as tk
from tkinter import messagebox
from utils import display_table

# Array to store billing information
billing = []

def open_billing():
    # Create new window for billing
    billing_window = tk.Toplevel()
    billing_window.title("Billing")
    billing_window.geometry("600x400")

    # Input fields for new billing
    tk.Label(billing_window, text="Patient Name").grid(row=0, column=0)
    patient_name = tk.Entry(billing_window)
    patient_name.grid(row=0, column=1)
    
    tk.Label(billing_window, text="Amount").grid(row=1, column=0)
    amount = tk.Entry(billing_window)
    amount.grid(row=1, column=1)
    
    tk.Label(billing_window, text="Date").grid(row=2, column=0)
    date = tk.Entry(billing_window)
    date.grid(row=2, column=1)

    # Add billing to array
    def add_billing():
        bill = {
            "patient_name": patient_name.get(),
            "amount": amount.get(),
            "date": date.get()
        }
        billing.append(bill)
        messagebox.showinfo("Success", "Billing Added")
        display_table(billing_window, billing)
        
    # Button to add billing
    tk.Button(billing_window, text="Add Billing", command=add_billing).grid(row=3, columnspan=2)

    # Display existing billing
    display_table(billing_window, billing)
