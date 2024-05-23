import tkinter as tk
from tkinter import filedialog
import sys

def select_file():
    # Create the main window
    root = tk.Tk()
    root.title("File Selector")

    # Set the window to be always on top
    root.attributes('-topmost', True)

    # Variable to store the file path
    file_path_var = tk.StringVar()

    # Create a label to display the file path
    file_label = tk.Label(root, textvariable=file_path_var, wraplength=400)
    file_label.pack(pady=20)

    def get_file_path():
        file_path = filedialog.askopenfilename()
        if file_path:
            file_path_var.set(file_path)
            print(f"Selected file: {file_path}")
            root.quit()  # Stop the Tkinter main loop
        else:
            print("File selection canceled. Exiting program.")
            root.destroy()  # Close the Tkinter window
            sys.exit()  # Exit the program

    # Call the get_file_path function when the program starts
    root.after(100, get_file_path)

    # Start the main event loop
    root.mainloop()

    return file_path_var.get()
