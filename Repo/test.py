import os
from pathlib import Path
import shutil

# folder path
dir_path = os.path.abspath (r'C:\Users\wjones25\Desktop\TEST')
count = 0
directory = "FOLDER_{}"
test2_path: str = r'C:\Users\wjones25\Desktop\test2'

 
def check_dir():
    count = 0
    # checking the directory for files
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print("checking dir")
    res1 = ('File count:', count)
    print(res1)
    if count <= 0:
        print("There are no files in the directory.")
    else:
        rname()
        folcreate()

def folcreate():
    print("There are still files in this directory.")
    os.mkdir(dir_path + directory.format(count + 1))
    print("Directory Created")
    move_file()
    # Loops back to begging until all files are removed from the dir_path
    check_dir()
    rname()

def move_file():
    file_names = os.listdir(dir_path)
    print("Moving files 12 at a time.")
    for file_names in file_names[:12]:
       # need to figure out the proper way to move to just created folder
        shutil.move(os.path.join(dir_path, file_names), test2_path)

# # need to rename the files extension to incrimneting number in 2 digit format
def rname(f=None):
    os.chdir(dir_path)
    print("Renaming Files.")
    print(os.getcwd())
    for count, f in enumerate(os.listdir()):
        f_name = os.path.splitext(f)[0]
        f_name = (f + str(count + 1))
       # f_name = (f + str(count + 1))
        br = (f_name[0:7] + str((count + 1, "{:02d}".format(count))))
        #print(f_name)
        print(br)
  #     new_name = f'{f_name}'
   #     print("break here")
    #    print(new_name)
       # os.rename(f, new_name)

#main
check_dir()
