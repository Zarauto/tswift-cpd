import tkinter as tk

def button_click(label):
    print(f"Button clicked: {label}")

root = tk.Tk()
root.title("Button List Example")

# Calculate window dimensions based on screen resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width / 2
window_height = (window_width * 9) / 16

# Set the window's geometry
root.geometry(f"{int(window_width)}x{int(window_height)}")

# Create a list of labels for buttons
button_labels = ["Button 1", "Button 2", "Button 3", "Button 4"]

# Create a frame to center the buttons
center_frame = tk.Frame(root)
center_frame.pack(expand=True)

# Create and place buttons in the center frame
for label_text in button_labels:
    button = tk.Button(center_frame, text=label_text, command=lambda label=label_text: button_click(label))
    button.pack(pady=10)

root.mainloop()
