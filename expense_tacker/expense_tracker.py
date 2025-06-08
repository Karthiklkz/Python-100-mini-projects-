import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("Income & Expense Tracker")
root.geometry("700x450")

# Global list to hold transactions
transactions = []
balance = 0.0

# Function to add income or expense
def add_transaction():
    global balance
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = category_entry.get()
    amount = amount_entry.get()
    trans_type = type_var.get()

    if category and amount:
        try:
            amount = float(amount)
            if trans_type == "Expense":
                amount = -abs(amount)
            else:
                amount = abs(amount)

            balance += amount

            transactions.append({
                "Date": date,
                "Category": category,
                "Amount": amount,
                "Type": trans_type,
                "Balance": balance
            })

            update_table()
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid input", "Amount must be a number")
    else:
        messagebox.showerror("Missing data", "Please enter category and amount")

# Function to update table
def update_table():
    for row in table.get_children():
        table.delete(row)
    for tx in transactions:
        table.insert("", tk.END, values=(tx["Date"], tx["Category"], tx["Amount"], tx["Type"], f"{tx['Balance']:.2f}"))
    balance_label.config(text=f"Current Balance: ₹{balance:.2f}")

# Function to save to CSV
def save_to_csv():
    if transactions:
        df = pd.DataFrame(transactions)
        df.to_csv("transactions.csv", index=False)
        messagebox.showinfo("Saved", "Transactions saved to transactions.csv")
    else:
        messagebox.showwarning("No data", "No transactions to save")

# --- UI Widgets ---

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Type:").pack()
type_var = tk.StringVar(value="Expense")
tk.OptionMenu(root, type_var, "Income", "Expense").pack()

tk.Button(root, text="Add Transaction", command=add_transaction).pack(pady=5)
tk.Button(root, text="Save to CSV", command=save_to_csv).pack(pady=5)

balance_label = tk.Label(root, text="Current Balance: ₹0.00", font=("Arial", 12, "bold"))
balance_label.pack(pady=5)

# Transaction Table
table = ttk.Treeview(root, columns=("Date", "Category", "Amount", "Type", "Balance"), show="headings")
for col in ("Date", "Category", "Amount", "Type", "Balance"):
    table.heading(col, text=col)
    table.column(col, width=100 if col != "Date" else 150)
table.pack(fill=tk.BOTH, expand=True)

root.mainloop()
