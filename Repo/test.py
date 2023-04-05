import os
from pathlib import Path
import shutil


# folder path
dir_path = r'C:\Users\Admin\Desktop\TEST'
count = 0
directory = "FOLDER_{}".format(count + 1)
test2_path = r'C:\Users\Admin\Desktop\test2'

#checking the directory for files
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
        
print('File count:', count)

#if there are files 
if count > 0:
    print("There are still files in this directory.") 
    os.mkdir(dir_path + directory)
    print("Directory '% s' created")

#moving files
    file_names = os.listdir(dir_path)
    for file_name in file_names[:12]:
        #need to figure out the proper way to move to just created folder
        shutil.move(os.path.join(dir_path, file_name),test2_path)


#need to rename the files extension to incrimneting number in 2 digit format
os.chdir(test2_path)
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name = os.path.splitext(f)
    f_name = f + str(count + 1)
    new_name = f'{f_name}'
    os.rename(f, new_name)

else:
    print ("There are no files in the directory.")
