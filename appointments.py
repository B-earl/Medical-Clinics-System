import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
from data import doctors, patients  # Import shared doctors and patients arrays
from utils import display_table

def open_appointments():
    # Create new window for appointments
    appointments_window = tk.Toplevel()
    appointments_window.title("Appointments")
    appointments_window.geometry("600x400")

    # Create a frame for the form (inputs)
    form_frame = tk.Frame(appointments_window)
    form_frame.pack(pady=10, padx=10)

    # Input fields for new appointment
    tk.Label(form_frame, text="Patient Name").grid(row=0, column=0, sticky="w", padx=5)
    patient_name = tk.Entry(form_frame)
    patient_name.grid(row=0, column=1, padx=5)

    tk.Label(form_frame, text="Doctor Name").grid(row=1, column=0, sticky="w", padx=5)
    # Doctor Name dropdown (populated from doctors array)
    doctor_names = [doctor["name"] for doctor in doctors]  # List of doctor names
    doctor_dropdown = ttk.Combobox(form_frame, values=doctor_names, width=17)
    doctor_dropdown.grid(row=1, column=1, padx=5)

    tk.Label(form_frame, text="Date").grid(row=2, column=0, sticky="w", padx=5)
    # Date Picker
    date = DateEntry(form_frame, width=17, background='darkblue', foreground='white', borderwidth=2)
    date.grid(row=2, column=1, padx=5)

    tk.Label(form_frame, text="Time").grid(row=3, column=0, sticky="w", padx=5)
    # Time Picker (hour and minute combo box)
    time_frame = tk.Frame(form_frame)
    time_frame.grid(row=3, column=1, padx=5, sticky="w")

    time_hour = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)], width=4)
    time_hour.grid(row=0, column=0, padx=5)
    time_hour.set("00")  # default to 00 for hours
    
    time_minute = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(0, 60, 5)], width=4)
    time_minute.grid(row=0, column=1, padx=5)
    time_minute.set("00")  # default to 00 for minutes

    # Symptoms Text Area
    tk.Label(form_frame, text="Symptoms").grid(row=4, column=0, sticky="w", padx=5)
    symptoms = tk.Text(form_frame, width=30, height=5)
    symptoms.grid(row=4, column=1, padx=5, pady=5)

    # Function to add appointment to patients array
    def add_appointment():
        # Ensure all fields are filled
        if not patient_name.get() or not doctor_dropdown.get():
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        appointment = {
            "patient_name": patient_name.get(),
            "doctor_name": doctor_dropdown.get(),  # Get selected doctor name
            "date": date.get_date(),  # Get selected date
            "time": f"{time_hour.get()}:{time_minute.get()}",  # Format time as "HH:MM"
            "symptoms": symptoms.get("1.0", "end-1c")  # Get symptoms from the text area
        }

        # Add appointment to patients array
        patients.append(appointment)
        messagebox.showinfo("Success", "Appointment Added")

        appointments_window.destroy()  # Close the window after success

    # Button to add appointment
    tk.Button(form_frame, text="Add Appointment", command=add_appointment).grid(row=5, columnspan=3, pady=10)
