import os
import shutil

src = '../os_exercises/'
dst = '../test/temp/one/two/'
# Virker både med absolute path som: 'C:/Users/Martin/Downloads/temp/one/two/' og fra current path: '/temp/one/two/'
def copyFiles(fromDirectory, targetDirectory):
    if targetDirectory.startswith('/'):
        targetDirectory = os.curdir + targetDirectory
  
    if not os.path.exists(targetDirectory):
        os.makedirs(targetDirectory)
    
    for entry in os.listdir(fromDirectory):
        print(entry)
        print(entry[0])
        # if entry[0] != '.':
        shutil.copy(fromDirectory + entry, targetDirectory + entry)


copyFiles(src, dst)