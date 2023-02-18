import sys
import os
import shutil

def execute(command):
    print(command)
    if len(command) == 4:
        copyFiles(command[1], command[3])

# Virker både med absolute path som: 'C:/Users/Martin/Downloads/temp/one/two/' og fra current path: '/temp/one/two/'
def copyFiles(fromDirectory, targetDirectory):
    if targetDirectory.startswith('/'):
        targetDirectory = os.curdir + targetDirectory
  
    if not os.path.exists(targetDirectory):
        os.makedirs(targetDirectory)
    
    for entry in os.listdir(fromDirectory):
        print(entry)
        shutil.copy(fromDirectory + entry, targetDirectory + entry)
    

execute(sys.argv)

