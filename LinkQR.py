import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import os
import webbrowser

# Function to open GitHub page
def open_github():
    webbrowser.open("https://github.com/AXIOM-SECURE")  # Replace with your GitHub page URL

# Function to generate QR code
def generate_qr():
    url = url_entry.get()
    fill_color = fill_color_var.get()
    back_color = back_color_var.get()
    
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Save the QR code as an image file
        img.save("LinkQR.png")
        
        # Display the QR code
        img = Image.open("LinkQR.png")
        img = img.resize((250, 250), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        qr_label.config(image=img)
        qr_label.image = img
        
        # Hide the style options and "Generate QR" button, show "Save QR" button
        fill_color_label.grid_forget()
        fill_color_menu.grid_forget()
        back_color_label.grid_forget()
        back_color_menu.grid_forget()
        generate_button.grid_forget()  # Hide the Generate QR button
        save_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL")

# Function to save QR code to a specified folder
def save_qr():
    url = url_entry.get()
    fill_color = fill_color_var.get()
    back_color = back_color_var.get()
    
    if url:
        folder_path = filedialog.askdirectory()
        if folder_path:
            file_path = os.path.join(folder_path, "LinkQR.png")
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save(file_path)
            messagebox.showinfo("Save QR Code", f"QR Code saved at {file_path}")
            
            # Reset the app
            url_entry.delete(0, tk.END)
            qr_label.config(image='')
            save_button.grid_forget()

            # Unhide the style options and "Generate QR" button
            fill_color_label.grid(row=2, column=0, pady=5, sticky="w")
            fill_color_menu.grid(row=2, column=1, pady=5, sticky="w")
            back_color_label.grid(row=4, column=0, pady=5, sticky="w")
            back_color_menu.grid(row=4, column=1, pady=5, sticky="w")
            generate_button.grid(row=5, column=1, columnspan=1, pady=15, sticky="w")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL")

# Setting up the UI
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x400")
root.configure(bg="black")

frame = tk.Frame(root, padx=10, pady=10, bg="black")
frame.pack(padx=10, pady=10, fill="both", expand=True)

url_label = tk.Label(frame, text="Enter URL:", fg="white", bg="black", font=("Helvetica", 12))
url_label.grid(row=0, column=0, pady=5, sticky="w")

url_entry = tk.Entry(frame, width=40, font=("Helvetica", 12))
url_entry.grid(row=0, column=1, pady=5, sticky="w")

generate_button = ttk.Button(frame, text="Generate QR", command=generate_qr, style="TButton")
generate_button.grid(row=5, column=1, columnspan=1, pady=15, sticky="w")

qr_label = tk.Label(frame, bg="black")
qr_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

# Color options
colors = ["black", "blue", "red", "green", "yellow", "purple", "white"]

fill_color_var = tk.StringVar(value="black")
fill_color_label = tk.Label(frame, text="Fill Color:", fg="white", bg="black", font=("Helvetica", 12))
fill_color_label.grid(row=2, column=0, pady=5, sticky="w")
fill_color_menu = ttk.OptionMenu(frame, fill_color_var, "black", *colors)
fill_color_menu.grid(row=2, column=1, pady=5, sticky="w")

back_color_var = tk.StringVar(value="white")
back_color_label = tk.Label(frame, text="BG Color:", fg="white", bg="black", font=("Helvetica", 12))
back_color_label.grid(row=4, column=0, pady=5, sticky="w")
back_color_menu = ttk.OptionMenu(frame, back_color_var, "white", *colors)
back_color_menu.grid(row=4, column=1, pady=5, sticky="w")

save_button = ttk.Button(frame, text="Save QR", command=save_qr, style="TButton")
# Initially hide the save button
save_button.grid_forget()

# Developer tag
dev_label = tk.Label(root, text="DEVELOPED BY AXIOM", font=("Arial", 8, "bold"), fg="grey", bg="black", cursor="hand2")
dev_label.pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=10)
dev_label.bind("<Button-1>", lambda e: open_github())  # Bind the click event

# Apply modern styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=6, relief="flat", background="white", foreground="black")
style.map("TButton",
          foreground=[("active", "black")],
          background=[("active", "white")])

root.mainloop()
