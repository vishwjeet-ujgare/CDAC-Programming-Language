# 4: Write a program to read from a file, pre-pending each line with "DIOT-" 
# and write to the different file 

from get_current_folder_path import current_path
path=current_path()

readFileA= open(path+"/fileB.txt","r")
fileAContent=readFileA.readlines()


# dataList=[]
# for line  in fileAContent:
#     dataList.append("DIOT-"+line)
   
readFileA.close()

print(fileAContent) 
with(open(path+"/fileC.txt","w") as file):
    for l in fileAContent:
        file.write("DIOT-"+l)
