from tkinter import *
from PIL import ImageTk, Image
import os

# Initialize the Tkinter window
root = Tk()
root.title("Python/Tkinter Image Viewer")
root.geometry("610x480")
root.iconbitmap("images/icon.ico")  # Ensure this file exists

# Load images dynamically from a folder
image_folder = "images"
image_files = [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png", ".jpeg"))]
image_list = [ImageTk.PhotoImage(Image.open(os.path.join(image_folder, f)).resize((600, 350))) for f in image_files]

# Counter for tracking current image
counter = 0

# Function to change image (Next/Previous)
def ChangeImage(direction):
    global counter
    if direction == "next":
        counter = (counter + 1) % len(image_list)
    elif direction == "prev":
        counter = (counter - 1) % len(image_list)

    imageLabel.config(image=image_list[counter])
    infoLabel.config(text=f"Image {counter + 1} of {len(image_list)} - {image_files[counter]}")

# UI Components
imageLabel = Label(root, image=image_list[counter])
infoLabel = Label(root, text=f"Image 1 of {len(image_list)} - {image_files[0]}", font=("Helvetica", 14))

# Buttons
prev_button = Button(root, text="Previous", width=10, bg="purple", fg="white", command=lambda: ChangeImage("prev"))
next_button = Button(root, text="Next", width=10, bg="purple", fg="white", command=lambda: ChangeImage("next"))

# Layout
imageLabel.pack()
infoLabel.pack()
prev_button.pack(side="left", padx=50, pady=5)
next_button.pack(side="right", padx=50, pady=5)

# Keyboard Bindings (Left/Right Arrow Keys)
root.bind("<Left>", lambda event: ChangeImage("prev"))
root.bind("<Right>", lambda event: ChangeImage("next"))

# Run the main loop
root.mainloop()