"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Derrick Swart.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding = 100, relief = 'raised')
    frame1.grid()
    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    hello_button = ttk.Button(frame1, text = 'Hello')
    hello_button.grid()
    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    hello_button['command']= (lambda:hello())
    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entry_box1 = ttk.Entry(frame1)
    entry_box1.grid()
    ok_goodbye_button = ttk.Button(frame1,text = 'Hello or Goodbye')
    ok_goodbye_button.grid()
    ok_goodbye_button['command'] = (lambda : hello_goodbye(entry_box1))
    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry_box2 = ttk.Entry(frame1)
    entry_box2.grid()
    number_button = ttk.Button(frame1, text='number of times')
    number_button.grid()
    number_button['command'] = (lambda: number_of_prints(entry_box1, entry_box2))
    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------
    fun = ttk.Button(frame1, text = 'fun button')
    fun.grid()
    fun['command'] = (lambda: fun_button())

    root.mainloop()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def hello():
    print('Hello')
def hello_goodbye(entry_box_1):
    contents_entry1 = entry_box_1.get()
    if contents_entry1 == 'ok':
        print('hello')
    else:
        print('goodbye')
def number_of_prints(entry1, entry2):
    entry1_contents = entry1.get()
    entry2_contents = entry2.get()
    for k in range (int(entry2_contents)):
        print(entry1_contents)
def fun_button():
    print('josh is no fun')
main()
