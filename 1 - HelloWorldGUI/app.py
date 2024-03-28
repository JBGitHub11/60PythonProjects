import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello World GUI Project")

    # Set the geometry (size)
    root.geometry("300x100")

    # Create a label widget with the text "Hello World"
    label = tk.Label(root, text="Hello World", font=("Arial", 16))

    # Pack the label into the window
    label.pack(expand=True)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
