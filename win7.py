import tkinter as tk
from tkinter import font

# ============================================================
# Create main window
root = tk.Tk()
root.title("Windows 7 OS")
root.geometry("600x400")
root.configure(bg='#2E8B57')      # Greenish desktop background

# ============================================================
# Fonts
win_font = font.Font(family="Segoe UI", size=10)
win_font_bold = font.Font(family="Segoe UI", size=10, weight="bold")

# ============================================================
# Desktop Icons (labels with blue text)
icon_frame = tk.Frame(root, bg='#2E8B57')
icon_frame.pack(side='left', anchor='nw', padx=20, pady=20)

computer_icon = tk.Label(icon_frame, text="🖥️ Computer", font=win_font,
                         bg='#2E8B57', fg='blue', cursor='hand2')
computer_icon.pack(anchor='w', pady=5)

recycle_icon = tk.Label(icon_frame, text="🗑️ Recycle Bin", font=win_font,
                        bg='#2E8B57', fg='blue', cursor='hand2')
recycle_icon.pack(anchor='w', pady=5)

docs_icon = tk.Label(icon_frame, text="📁 My Documents", font=win_font,
                     bg='#2E8B57', fg='blue', cursor='hand2')
docs_icon.pack(anchor='w', pady=5)

# ============================================================
# Taskbar (bottom)
taskbar = tk.Frame(root, bg='#1E2E4F', height=40)
taskbar.pack(side='bottom', fill='x')

# Start button – now BLUE background with BLACK text
start_btn = tk.Button(taskbar, text="Start", font=win_font_bold,
                      bg='blue', fg='black', relief='raised',
                      activebackground='#4a7db5', bd=2,
                      command=lambda: print("Start clicked"))
start_btn.pack(side='left', padx=5, pady=5)

# Quick launch separator
sep = tk.Label(taskbar, text="   |   ", font=win_font,
               bg='#1E2E4F', fg='white')
sep.pack(side='left')

# Tray area with clock
tray_frame = tk.Frame(taskbar, bg='#1E2E4F')
tray_frame.pack(side='right', padx=10)

def update_clock():
    from datetime import datetime
    now = datetime.now().strftime("%I:%M %p")
    clock_label.config(text=now)
    root.after(1000, update_clock)

clock_label = tk.Label(tray_frame, text="", font=win_font,
                       bg='#1E2E4F', fg='white')
clock_label.pack(side='right')
update_clock()

# ============================================================
# Welcome dialog – OK button now BLUE with BLACK text
welcome_frame = tk.Frame(root, bg='#F0F0F0', relief='groove', bd=3)
welcome_frame.place(relx=0.5, rely=0.4, anchor='center', width=300, height=120)

welcome_title = tk.Label(welcome_frame, text="Welcome to Windows 7",
                         font=win_font_bold, bg='#F0F0F0', fg='blue')
welcome_title.pack(pady=10)

welcome_msg = tk.Label(welcome_frame,
                       text="Your simulated Windows 7 desktop\nis ready.",
                       font=win_font, bg='#F0F0F0', fg='black')
welcome_msg.pack(pady=5)

close_btn = tk.Button(welcome_frame, text="OK", font=win_font,
                      bg='blue', fg='black', activebackground='#4a7db5',
                      command=welcome_frame.destroy)
close_btn.pack(pady=10)

# ============================================================
root.mainloop()
