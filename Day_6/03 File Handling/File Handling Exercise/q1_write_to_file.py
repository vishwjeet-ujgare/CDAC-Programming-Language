
# 1: write a program to take some text lines from the user and write it to the file

from get_current_folder_path import current_path

text=input("Please enter your text : ")
path=current_path()+"/fileA.txt"

with (open(path,'w') as file):
    file.write(text)
    file.close()
    
    