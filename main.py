import tkinter as tk
from appointments import open_appointments
from patients import open_patients
from doctors import open_doctors
from billing import open_billing

def create_dashboard():
    # Create the main window
    root = tk.Tk()
    root.title("Medical Clinic System")
    root.geometry("800x600")

    # Add the main label
    dashboard_label = tk.Label(root, text="Welcome to the Medical Clinic System", font=("Arial", 20))
    dashboard_label.pack(pady=20)

    # Buttons to open each window
    tk.Button(root, text="Appointments", width=20, height=2, command=open_appointments).pack(pady=10)
    tk.Button(root, text="Patients", width=20, height=2, command=open_patients).pack(pady=10)
    tk.Button(root, text="Doctors", width=20, height=2, command=open_doctors).pack(pady=10)
    tk.Button(root, text="Billing", width=20, height=2, command=open_billing).pack(pady=10)

    # Start the application
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
