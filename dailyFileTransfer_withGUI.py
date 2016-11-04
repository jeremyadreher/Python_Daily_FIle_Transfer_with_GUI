from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import shutil

class dftGUI:

    def __init__(self, master):

        master.title('Daily File Transfer')
        master.resizable(False, False)
        master.configure()

        self.style = ttk.Style()
        self.style.configure('Instructions.TLabel', font = (12))


        # Instructions
        self.inst_frame = ttk.Frame(master)
        self.inst_frame.pack()
        self.l1 = ttk.Label(self.inst_frame, text = 'INSTRUCTIONS', font = ("Arial", 14))
        self.l2 = ttk.Label(self.inst_frame, text = "1. Click the 'Browse For Source' button to select a folder to check and copy files from.", font = ("Arial", 10))
        self.l3 = ttk.Label(self.inst_frame, text = "2. Click the 'Browse For Destination' button to select a folder to copy files from", font = ("Arial", 10))
        self.l4 = ttk.Label(self.inst_frame, text = "3. Click 'Initiate File Check & Copy' button to execute the program.", font = ("Arial", 10))
        self.l1.grid(row = 0, column = 0, columnspan = 2)
        self.l2.grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
        self.l3.grid(row = 2, column = 0, columnspan = 2, sticky = 'w')
        self.l4.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
        
        # Browse & Select Source and Destination Folders for File Check
        self.browse_frame = ttk.Frame(master)
        self.browse_frame.pack()
        sourceButton = ttk.Button(self.browse_frame, text = 'Browse For Source', command = self.selectSource).grid(row = 0, column = 0)
        destButton = ttk.Button(self.browse_frame, text = 'Browse For Destination', command = self.selectDest).grid(row = 0, column = 2)
        srcPath = StringVar()
        dstPath = StringVar()
        ttk.Label(self.browse_frame, textvariable = srcPath).grid(row = 1, column = 0)
        ttk.Label(self.browse_frame, textvariable = dstPath).grid(row = 1, column = 2)

        # Initiate File Check
        self.init_frame = ttk.Frame(master)
        self.init_frame.pack()
        initButton = ttk.Button(self.init_frame, text = 'Initiate File Check & Copy', command = self.initFileCheck).grid(row = 0, column = 0, columnspan = 2)

    def selectSource(self):
        self.src = filedialog.askdirectory()
        self.srcPath = self.src
     
    def selectDest(self):
        self.dst = filedialog.askdirectory()
        dstPath = self.dst
   
    def move_files(self, sourcePath, destPath):
        source = os.listdir(sourcePath)
        for files in source:
                    source_files = os.path.join(sourcePath, files)
                    dest_files = os.path.join(destPath, files)
                    modTime = os.path.getmtime(source_files)
                    currentTime = time.time()
                    twentyFourHoursAgo = currentTime - 86400
                    if files.endswith('.txt') and modTime > twentyFourHoursAgo:
                        source_files = os.path.join(sourcePath, files)
                        dest_files = os.path.join(destPath, files)
                        shutil.copy(source_files,destPath)
                        
    def initFileCheck(self):
        print (self.src)
        print (self.dst)
        self.move_files(self.src,self.dst)
        messagebox.showinfo(title = 'Daily File Transfer', message = 'Files successfully copied!')

def main():
        master = Tk()
        dailyFileTransfer = dftGUI(master)
        master.mainloop()
        
        

if __name__=='__main__': main()
