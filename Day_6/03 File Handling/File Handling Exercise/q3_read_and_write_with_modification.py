# 3: Write a program to read from a file and modify each of its line
# by pre-pending each line with "DIOT-" 

# ex: 
# i/p : hello
#       good morning  

# o/p:      DIOT-hello
#           DIOT-good morning  


from get_current_folder_path import current_path
path=current_path()

readFileA= open(path+"/fileA.txt","r")
fileAContent=readFileA.readlines()


# dataList=[]
# for line  in fileAContent:
#     dataList.append("DIOT-"+line)
   
readFileA.close()

print(fileAContent) 
with(open(path+"/fileA.txt","w") as file):
    for l in fileAContent:
        file.write("DIOT-"+l)




  
