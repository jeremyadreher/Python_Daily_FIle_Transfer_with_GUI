import os
import time
import shutil



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

if __name__=='__main__':
    main()
