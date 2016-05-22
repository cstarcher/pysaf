#!/usr/bin/env python3

"""Main file to be called first."""

import tkinter as tk
import gui
import guiwin
import getset
import platform

if __name__ == '__main__':
    root = tk.Tk()
    gs = getset.GetSet()
    if platform.system() == 'Windows':
        guiwin.GuiTk(root, gs)
    else:
        gui.GuiTk(root, gs)
    root.mainloop()
