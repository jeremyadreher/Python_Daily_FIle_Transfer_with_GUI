from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os
import time
import shutil


def selectFolder():
    askdirectory()
    

def move_files(sourcePath, destPath):
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

def main():
    src = 'C:\\LocalSourceFiles\\Python_Daily_File_Transfer\\Daily'
    dst = 'C:\\LocalSourceFiles\\Python_Daily_File_Transfer\\Home_Office'
    move_files(src,dst)


def makeWindow():
    root = Tk()
    root.title('Daily File Transfer')
    root.resizable(False, False)
    root.configure()

    style = ttk.Style()
    style.configure('Instructions.TLabel', font = (12))


    # Instructions
    frame1 = Frame(root)
    frame1.pack()
    Label(frame1, text = 'INSTRUCTIONS',
                  font = ("Arial", 14)).grid(row = 0, column = 0, columnspan = 2)
    Label(frame1, text = "1. Click the 'Browse For Source' button to select a folder to check and copy files from.",
                  font = ("Arial", 10)).grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
    Label(frame1, text = "2. Click the 'Browse For Destination' button to select a folder to copy files from",
                  font = ("Arial", 10)).grid(row = 2, column = 0, columnspan = 2, sticky = 'w')
    Label(frame1, text = "3. Click 'Initiate File Check & Copy' button to execute the program.",
                  font = ("Arial", 10)).grid(row = 3, column = 0, columnspan = 2, sticky = 'w')


    # Browse & Select Source and Destination Folders for File Check
    frame2 = Frame(root)
    frame2.pack()
    sourceButton = Button(frame2, text = 'Browse For Source', command = selectFolder).grid(row = 0, column = 0)
    destButton = Button(frame2, text = 'Browse For Destination', command = selectFolder).grid(row = 0, column = 2)
    Label(frame2).grid(row = 1, column = 0)
    Label(frame2).grid(row = 1, column = 2)


    # Initiate File Check
    frame3 = Frame(root)
    frame3.pack()
    Button(frame3, text = 'Initiate File Check & Copy').grid(row = 0, column = 0, columnspan = 2)


if __name__=='__main__':
    main()



