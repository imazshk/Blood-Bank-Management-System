import tkinter as tk
from tkinter import messagebox
from BloodBank import BloodBank  # Assuming you have a BloodBank module

def getbloodtype(num):
    blood_dictionary = {1: "A+", 2: "A-", 3: "B+", 4: "B-", 5: "O+", 6: "O-", 7: "AB+", 8: "AB-"}
    return blood_dictionary.get(num)

def add_donor():
    try:
        donor_name = entry_donor_name.get()
        donor_age = int(entry_donor_age.get())
        temp = int(var_donor_blood_type.get())
        donor_blood_type = getbloodtype(temp)
        BloodBank.donor_details(donor_name, donor_age, donor_blood_type)
        messagebox.showinfo("Success", "Donor details added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def request_blood():
    try:
        hospital_name = entry_hospital_name.get()
        patient_name = entry_patient_name.get()
        patient_age = int(entry_patient_age.get())
        temp = int(var_patient_blood_type.get())
        patient_blood_type = getbloodtype(temp)
        donor_name = entry_request_donor_name.get()
        donor_age = int(entry_request_donor_age.get())
        temp = int(var_request_donor_blood_type.get())
        donor_blood_type = getbloodtype(temp)
        BloodBank.request_blood(hospital_name, patient_name, patient_age, patient_blood_type, donor_name, donor_age, donor_blood_type)
        messagebox.showinfo("Success", "Blood requested successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def show_add_donor_frame():
    frame_add_donor.pack(fill="both", expand=1)
    frame_request_blood.pack_forget()

def show_request_blood_frame():
    frame_request_blood.pack(fill="both", expand=1)
    frame_add_donor.pack_forget()

root = tk.Tk()
root.title("AIB Blood Bank")

frame_add_donor = tk.Frame(root)
frame_request_blood = tk.Frame(root)

# Add Donor Frame
tk.Label(frame_add_donor, text="Add Donor Details", font=('Helvetica', 16)).pack(pady=10)
tk.Label(frame_add_donor, text="Donor Name:").pack()
entry_donor_name = tk.Entry(frame_add_donor)
entry_donor_name.pack()

tk.Label(frame_add_donor, text="Donor Age:").pack()
entry_donor_age = tk.Entry(frame_add_donor)
entry_donor_age.pack()

tk.Label(frame_add_donor, text="Blood Type:").pack()
var_donor_blood_type = tk.StringVar(frame_add_donor)
options = {1: "A+", 2: "A-", 3: "B+", 4: "B-", 5: "O+", 6: "O-", 7: "AB+", 8: "AB-"}
for val, blood_type in options.items():
    tk.Radiobutton(frame_add_donor, text=blood_type, variable=var_donor_blood_type, value=val).pack(anchor=tk.W)

tk.Button(frame_add_donor, text="Submit", command=add_donor).pack(pady=10)

# Request Blood Frame
tk.Label(frame_request_blood, text="Request Blood", font=('Helvetica', 16)).pack(pady=10)
tk.Label(frame_request_blood, text="Hospital Name:").pack()
entry_hospital_name = tk.Entry(frame_request_blood)
entry_hospital_name.pack()

tk.Label(frame_request_blood, text="Patient Name:").pack()
entry_patient_name = tk.Entry(frame_request_blood)
entry_patient_name.pack()

tk.Label(frame_request_blood, text="Patient Age:").pack()
entry_patient_age = tk.Entry(frame_request_blood)
entry_patient_age.pack()

tk.Label(frame_request_blood, text="Patient Blood Type:").pack()
var_patient_blood_type = tk.StringVar(frame_request_blood)
for val, blood_type in options.items():
    tk.Radiobutton(frame_request_blood, text=blood_type, variable=var_patient_blood_type, value=val).pack(anchor=tk.W)

tk.Label(frame_request_blood, text="Donor Name:").pack()
entry_request_donor_name = tk.Entry(frame_request_blood)
entry_request_donor_name.pack()

tk.Label(frame_request_blood, text="Donor Age:").pack()
entry_request_donor_age = tk.Entry(frame_request_blood)
entry_request_donor_age.pack()

tk.Label(frame_request_blood, text="Donor Blood Type:").pack()
var_request_donor_blood_type = tk.StringVar(frame_request_blood)
for val, blood_type in options.items():
    tk.Radiobutton(frame_request_blood, text=blood_type, variable=var_request_donor_blood_type, value=val).pack(anchor=tk.W)

tk.Button(frame_request_blood, text="Submit", command=request_blood).pack(pady=10)

# Navigation Buttons
tk.Button(root, text="Add Donor", command=show_add_donor_frame).pack(side="left", padx=20, pady=20)
tk.Button(root, text="Request Blood", command=show_request_blood_frame).pack(side="right", padx=20, pady=20)

show_add_donor_frame()

root.mainloop()
