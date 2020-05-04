#Module:  XXXX
#SubComponet:   XXXX
#COMPONET:  gui
#Projet:    Generic updateHelper

#Author:    Noah Fouts
#Version:   0.0.1.0
#Version Name:  INDEV 0.1
#Updated:   2020-07-01T6:00 PM PST

#This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import tkinter
from tkinter import ttk
import time

#Start Logger
logger = logging.getLogger("updateHelper")

#GUI
def startGUI():
    logger.debug("Recieved call to startGUI")

    logger.debug("Starting startupscreen")
    root = tkinter.Tk()
    sS = startupScreen(master=root)
    root.after(1500, lambda: root.destroy())
    sS.mainloop()
    logger.debug("StartupScreen completed.")

    logger.debug("Startin main window")
    root = tkinter.Tk()
    mW = mainWindow(master=root)
    mW.mainloop()
    logger.debug("Main Winodow exited.")

class startupScreen(tkinter.Frame):
    def __init__(self, master=None):
        logger.debug("Loading startup screen.")
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tkinter.PhotoImage(file='gui\images\BSILogo.png')
        self.logoBox = tkinter.Label(master=self.master, image=self.Logo)
        #self.logoBox.image = self.Logo
        self.logoBox.pack(side='top')
        self.text = tkinter.Label(master=self.master,text="Loading...")
        self.text.pack(side='top')

class mainWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.discoveryBar = ttk.Progressbar(self.master, orient = 'horizontal', length = 100, mode = 'indeterminate')
        self.discoveryBar.pack()
        self.time = 0

    def updateDiscoveryBar(self):
        if(self.time < 100):
            self.time += 5
        else:
            self.time -= 100
        self.discoveryBar['value'] = self.time
        self.master.update_idletasks() 
