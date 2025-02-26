import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from appointments import open_appointments
from patients import open_patients
from doctors import open_doctors
from billing import open_billing

def create_dashboard():
    # Create the main window
    root = tk.Tk()
    root.title("Medical Clinic System")
    root.geometry("800x500")
    
    # Load background image
    bg_image = Image.open("background.jpg") 
    bg_image = bg_image.resize((800, 500), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create Canvas for background
    canvas = tk.Canvas(root, width=800, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)

    # Create a semi-transparent overlay frame
    container = tk.Frame(root, bg="white", padx=40, pady=40, relief="ridge", bd=2)
    container.place(relx=0.5, rely=0.5, anchor="center")

    # Main title label
    dashboard_label = tk.Label(
        container, text="Medical Clinic System", font=("Arial", 22, "bold"), bg="white", fg="#333"
    )
    dashboard_label.pack(pady=(0, 20))

    # Button styling
    button_style = {
        "font": ("Arial", 14, "bold"),
        "width": 25,
        "height": 2,
        "bg": "#007BFF",
        "fg": "white",
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2",
    }

    # Hover effects for buttons
    def on_enter(e): e.widget.config(bg="#0056b3")
    def on_leave(e): e.widget.config(bg="#007BFF")

    # Create buttons dynamically
    buttons = [
        ("\U0001F4C5 Appointments", open_appointments),  # 📅 Unicode emoji for better rendering
        ("\U0001F468\u200D⚕️ Patients", open_patients),  # 🧑‍⚕️ Unicode emoji
        ("\U0001F468\u200D⚕️ Doctors", open_doctors),  # 👨‍⚕️ Unicode emoji
        ("\U0001F4B3 Billing", open_billing),  # 💳 Unicode emoji
    ]

    for text, command in buttons:
        btn = tk.Button(container, text=text, command=command, **button_style)
        btn.pack(pady=10, fill="x")
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
