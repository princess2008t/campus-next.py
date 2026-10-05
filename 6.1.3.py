import tkinter as tk

root = tk.Tk()
root.title("My Favorite Video")

label = tk.Label(
    root,
    text="What's my favorite video?",
    fg="#FF69B4",
    font=("Arial", 16)
)
label.pack(pady=10)
image = tk.PhotoImage(file="favorite.png")
def show_image():
    image_label = tk.Label(root, image=image)
    image_label.pack(pady=10)

button = tk.Button(
    root,
    text="Click to find out!",
    width=25,
    bg="#FF69B4",
    fg="white",
    command=show_image
)
button.pack(pady=10)

root.mainloop()