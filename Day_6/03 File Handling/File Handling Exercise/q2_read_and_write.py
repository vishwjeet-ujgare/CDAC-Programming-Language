# 2: write a program to read from a file and write to another file 
from get_current_folder_path import current_path
path=current_path()

readFileA= open(path+"/fileA.txt","r")
fileAContent=readFileA.read()
readFileA.close()


with( open(current_path()+"/fileB.txt","w") as fileB):
    fileB.write(fileAContent)


