import json
import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os
import subprocess

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

def save_config():
    try:
        config = {
            "seed": int(seed_entry.get()),
            "num_communities": int(comm_entry.get()),
            "people_per_community": int(people_entry.get()),
            "kill_prob": float(kill_entry.get()),
            "infect_prob": float(infect_entry.get()),
            "infect_inmune_prob": float(infect_immune_entry.get()),
            "min_cure_days": int(min_cure_entry.get()),
            "max_cure_days": int(max_cure_entry.get())
        }
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")
        return
    
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    messagebox.showinfo("Success", "Config saved to config.json")
    
def run_main():
    python_executable = sys.executable
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"src/main.py")
    try:
        subprocess.Popen([python_executable, script_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run simulation:\n{e}")
        return

    root.destroy()

root = tk.Tk()
root.title("Simulation Configuration")
root.geometry("400x420")
root.resizable(True, True)
root.configure(bg="#191D21")  # dark background for root

style = ttk.Style(root)
style.theme_use('clam')

# Set Frame background to dark (this affects the container frame)
style.configure('TFrame', background="#191D21")

# Labels with background matching frame and light text color
style.configure('TLabel', background="#191D21", foreground="#AFC2E6", font=('Segoe UI', 11))

# Entries with dark background and lighter text
style.configure('TEntry',
                fieldbackground="#2E3440",  # entry background
                foreground="#C9D7F3",       # text color
                font=('Segoe UI', 11))

# Buttons with dark background and lighter foreground
style.configure('TButton',
                background="#4E80B2",
                foreground="#FFFFFF",
                font=('Segoe UI', 11),
                padding=6)

# To ensure button background shows, map its colors on active and pressed states:
style.map('TButton',
          background=[('active', '#357ABD'), ('pressed', '#2E5597')],)

frame = ttk.Frame(root, padding=20, style='TFrame')
frame.pack(fill=tk.BOTH, expand=True)

labels = [
    "Random seed",
    "Number of communities",
    "People per community",
    "Kill probability",
    "Infection probability",
    "Infection probability (immune)",
    "Min cure days",
    "Max cure days"
]

entries = []

for i, label in enumerate(labels):
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=6)
    entry = ttk.Entry(frame, width=25)
    entry.grid(row=i, column=1, pady=6, padx=(10,0))
    entries.append(entry)

(seed_entry, comm_entry, people_entry, kill_entry,
 infect_entry, infect_immune_entry, min_cure_entry, max_cure_entry) = entries

button_frame = ttk.Frame(frame, style='TFrame')
button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)

save_button = ttk.Button(button_frame, text="Save Config", command=save_config)
save_button.pack(side=tk.LEFT, padx=10)

run_button = ttk.Button(button_frame, text="Run Simulation", command=run_main)
run_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
