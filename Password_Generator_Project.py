from tkinter import *
from tkinter.ttk import *
import random, string
import pyperclip

# Initialize Window
window = Tk()
window.title("Password Generator")
window.geometry("350x400")
window.resizable(0, 0)

Label(window, text="🔐 PASSWORD GENERATOR", font="arial 15 bold").pack(pady=10)

# Password Length Input
pass_label = Label(window, text="PASSWORD LENGTH", font="arial 10 bold").pack()
pass_len = IntVar(value=8)  # Default length 8
length = Spinbox(window, from_=0, to_=32, textvariable=pass_len, width=10)
length.pack(pady=5)

# Password Display
pass_str = StringVar()
Entry(window, textvariable=pass_str, font="arial 12", justify="center", width=30, state="readonly").pack(pady=5)

# Password Strength Label
strength_label = Label(window, text="", font="arial 10 bold")
strength_label.pack()


def check_strength(password):
    """Check password strength based on length & character variety"""
    length_score = min(pass_len.get() // 4, 3)  # Max score of 3 for length
    variety_score = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ])

    score = length_score + variety_score

    if score >= 6:
        return "🟢 Strong"
    elif score >= 4:
        return "🟡 Medium"
    else:
        return "🔴 Weak"


def generate_password():
    """Generates a secure password with at least one uppercase, lowercase, digit, and symbol"""
    password = []

    if pass_len.get() >= 4:
        password.extend([
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ])

    password.extend(random.choice(string.ascii_letters + string.digits + string.punctuation)
                    for _ in range(pass_len.get() - len(password)))

    random.shuffle(password)
    generated_password = ''.join(password)

    pass_str.set(generated_password)
    strength_label.config(text=f"Strength: {check_strength(generated_password)}")


def copy_password():
    """Copy password to clipboard & show confirmation"""
    pyperclip.copy(pass_str.get())
    strength_label.config(text="✅ Copied to Clipboard!")


# Buttons
Button(window, text="GENERATE PASSWORD", command=generate_password).pack(pady=5)
Button(window, text="COPY TO CLIPBOARD", command=copy_password).pack(pady=5)

# Run Tkinter Loop
window.mainloop()
