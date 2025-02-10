from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()  # Create the main window
        self.root.title("My Window")  # Set the window title

        self.canvas = Canvas(self.root, width=width, height=height)  # Create a Canvas widget
        self.canvas.pack(fill=BOTH, expand=True)  # Expand canvas to fill the window

        self.running = False  # Initialize the "running" flag

    def redraw(self):
        """Force the window to redraw itself."""
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        """Keep the window open until the user closes it."""
        self.running = True  # Set running state to True
        while self.running:
            self.redraw()  # Continuously redraw the window

    def close(self):
        """Close the window by setting running state to False."""
        self.running = False  # Stop the loop in wait_for_close()