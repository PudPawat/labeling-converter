import os
# path = "home/airlab/Desktop/mirror20220614/20220614/backlight1"
path = "F:\\Ph.D\\mirror\\data\\20220628"
add_name = path.split("/")[-1]
folder_list = ["img_24062022","img_RGB","xml","combine_contactlens1","original1", "images","XML"]
listdir = os.listdir(path)
""
print(listdir)

for folder_light in listdir:
    path_folder_lighr = os.path.join(path,folder_light)
    listdir_sub = os.listdir(path_folder_lighr)
    add_name = folder_light
    for name in listdir_sub:
        for folder in folder_list:
            if name == folder:
                path2file = os.path.join(path_folder_lighr,folder)
                namein_folder  = os.listdir(path2file)

                for name_file in namein_folder:
                    os.rename(os.path.join(path2file,name_file),os.path.join(path2file,add_name+name_file))