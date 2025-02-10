from Window_Class import Window  # Import the Window class

def main():
    win = Window(800, 600)  # Create a window of 800x600 pixels
    win.wait_for_close()  # Keep it open until the user closes it

if __name__ == "__main__":
    main()  # Run the main function