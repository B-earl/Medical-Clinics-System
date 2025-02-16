import tkinter as tk
from tkinter import messagebox
from data import doctors  # Import shared doctors array

def open_doctors():
    # Create new window for doctors
    doctors_window = tk.Toplevel()
    doctors_window.title("Doctors")
    doctors_window.geometry("600x400")

    # Create a frame for the form (inputs)
    form_frame = tk.Frame(doctors_window)
    form_frame.pack(pady=10, padx=10)

    # Input fields for new doctor
    tk.Label(form_frame, text="Doctor Name").grid(row=0, column=0, sticky="w", padx=5)
    doctor_name = tk.Entry(form_frame)
    doctor_name.grid(row=0, column=1, padx=5)
    
    tk.Label(form_frame, text="Specialty").grid(row=1, column=0, sticky="w", padx=5)
    specialty = tk.Entry(form_frame)
    specialty.grid(row=1, column=1, padx=5)
    
    tk.Label(form_frame, text="Phone").grid(row=2, column=0, sticky="w", padx=5)
    phone = tk.Entry(form_frame)
    phone.grid(row=2, column=1, padx=5)

    # Function to add doctor to array and update table
    def add_doctor():
        doctor = {
            "name": doctor_name.get(),
            "specialty": specialty.get(),
            "phone": phone.get()
        }
        doctors.append(doctor)
        messagebox.showinfo("Success", "Doctor Added")

        doctors_window.destroy()
        
        # Display updated doctor table
        display_doctor_table()

    # Button to add doctor
    tk.Button(form_frame, text="Add Doctor", command=add_doctor).grid(row=3, columnspan=2, pady=10)

    # Create a frame for displaying the table of doctors
    table_frame = tk.Frame(doctors_window)
    table_frame.pack(pady=10)

    # Function to display doctors in a table
    def display_doctor_table():
        # Clear previous table content
        for widget in table_frame.winfo_children():
            widget.grid_forget()

        # Table headers
        headers = ["Doctor Name", "Specialty", "Phone"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=('Arial', 10, 'bold')).grid(row=0, column=col, padx=5, pady=5)

        # Populate the table with doctors
        for i, doctor in enumerate(doctors):
            row = i + 1
            tk.Label(table_frame, text=doctor["name"]).grid(row=row, column=0, padx=5, pady=5)
            tk.Label(table_frame, text=doctor["specialty"]).grid(row=row, column=1, padx=5, pady=5)
            tk.Label(table_frame, text=doctor["phone"]).grid(row=row, column=2, padx=5, pady=5)

    # Initial display of the doctor table (if any doctors are already added)
    display_doctor_table()

    doctors_window.mainloop()
