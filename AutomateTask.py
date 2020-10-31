import shutil
import os

source_path = input("Pls give the path of a Folder you want to take Backup : ")
back_path = input(
    "Pls give the path of a Folder where you want to store the Backup : ")

listOfItems = os.listdir(source_path)

for i in listOfItems:
    FileName, Extension = os.path.splitext(i)
    if(Extension == '' or Extension == 'pc'):
        continue
    path = source_path+'/'+i
    dest_path = back_path+'/'
    shutil.copy(path, dest_path)

print("Copied The Files and Sorting them!!")

listOfItems2 = os.listdir(back_path)

for i in listOfItems2:
    FileName, Extension = os.path.splitext(i)
    if(Extension == ''):
        continue

    finalPath = back_path + '/' + Extension
    exist = os.path.exists(finalPath)
    if(exist == False):
        os.mkdir(finalPath)
    shutil.move(back_path+'/'+i, finalPath+'/'+i)

print("Sorting Completed!!")
print("Congratulations !! All your files are Ready")
