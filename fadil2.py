'''import tkinter as tk

def calculate_payment():
    total_amount = float(entry_total_amount.get())
    num_members = int(entry_num_members.get())
    payment_per_person = total_amount / num_members
    label_result.config(text=f"Each person should pay: ${payment_per_person:.2f}")

root = tk.Tk()
root.title("Resource Distribution System for PG(s)")

label_title = tk.Label(root, text="Resource Distribution System for PG(s)")
label_title.pack()

button_create_plan = tk.Button(root, text="Create Plan", command=calculate_payment)
button_create_plan.pack()

label_num_members = tk.Label(root, text="Enter the number of members:")
label_num_members.pack()
entry_num_members = tk.Entry(root)
entry_num_members.pack()

label_total_amount = tk.Label(root, text="Enter the total amount per month:")
label_total_amount.pack()
entry_total_amount = tk.Entry(root)
entry_total_amount.pack()

button_calculate = tk.Button(root, text="Calculate Payment", command=calculate_payment)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
'''
import tkinter as tk

def calculate_payment():
    total_members = int(entry_members.get())
    total_amount = float(entry_amount.get())
    payment_per_person = total_amount / total_members
    result_label.config(text=f"Each person should pay: ₹{payment_per_person:.2f}",font=('Dubai',20))

def create_plan_window():
    plan_window = tk.Toplevel(root)
    plan_window.title("Create Plan")
    plan_window.geometry('800x500')

    global entry_members, entry_amount, result_label

    label=tk.Label(plan_window, text="Number of Members:",font=("Arial",14))
    label.pack(padx=20, pady=20)
    entry_members = tk.Entry(plan_window)
    entry_members.pack()

    label=tk.Label(plan_window, text="Total Amount per Month:",font=("Arial",14))
    label.pack(padx=20, pady=20)
    entry_amount = tk.Entry(plan_window)
    entry_amount.pack()

    tk.Button(plan_window, text="Calculate Payment" ,font=("Arial",18), command=calculate_payment).pack()

    result_label = tk.Label(plan_window, text="")
    result_label.pack()

root = tk.Tk()
root.geometry('800x500')
root.title("Resource Distribution System for PG(s)" )
canvas = tk.Canvas(root, width=800, height=800, bg="lightblue")


title_label = tk.Label(root, text="Resource Distribution System for PG(s)",font=('Gabriola',18))
title_label.pack()


create_plan_button = tk.Button(root, text="Create Plan", command=create_plan_window)
create_plan_button.pack()

root.mainloop()
