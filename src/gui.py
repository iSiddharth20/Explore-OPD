'''
Tkinter based GUI
Talks to Main, PreProcess, DB
'''

# Import Necessary Libraries
import tkinter as tk


class GUI:
    def __init__(self, appname="Your App Name", width=600, height=400):
        self.window = tk.Tk()
        self.window.title(appname)
        self.window.geometry(f"{width}x{height}")

    def action_button(self, text="Action Button", command=lambda: print("Action Button Clicked")):
        """ Click Button To Perform Action"""
        button = tk.Button(self.window, text=text, command=command)
        return button

    def start(self):
        """ Start the Tkinter event loop """
        self.window.mainloop()


if __name__ == "__main__":
    testrun = GUI()
    testrun.action_button().pack()
    testrun.start()

