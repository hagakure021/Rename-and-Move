import os
from pathlib import Path
import shutil

# folder path
dir_path = os.path.abspath(r'C:\Users\Admin\Documents\GitHub\Rename-and-Move\Repo\TEST')
count = 0
directory = "FOLDER_{}"
test2_path: str = r'C:\Users\Admin\Documents\GitHub\Rename-and-Move\Repo\test2'


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



def rname():
    os.chdir(dir_path)
    print("Renaming Files.")
    #print(os.getcwd())
    for index, f in enumerate(os.listdir()):
        f_name = os.path.splitext(f)[0]
        ext_name = os.path.splitext(f)[1]
        br = f_name[0:7] + "{:02d}".format((index % 12) + 1)
        new_name = f'{br}{ext_name}'
        os.rename(f, new_name)
    print("Moving to folder create")
    folcreate()
   # move_file()

def folcreate():
    print("There are still files in this directory.")
    isExist = os.path.exists(dir_path + directory.format(count + 1))
    print(isExist)
    os.mkdir(dir_path + directory.format(isExist + 1))
    print("Directory Created")
    print("Moving to move file")
    move_file()

    # Loops back to begging until all files are removed from the dir_path

def move_file():
    file_names = os.listdir(dir_path)
    print(file_names)
    print("Moving files 12 at a time.")
    for file_names in file_names[:12]:
        # need to figure out the proper way to move to just created folder
        shutil.move(os.path.join(dir_path, file_names), test2_path)
    print('Finishing move restarting check')
    check_dir()




# main
check_dir()
