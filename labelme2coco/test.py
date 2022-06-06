'''
HOW TO Open labelme
open Anaconda or python cmd
type labelme
'''
import glob

# import package
# from labelme2coco import labelme2coco
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "F:\Ph.D\mirror\data\march2-2022-20220303T122905Z-001\march2-2022"

# set path for coco json to be saved
save_json_path = ""
# labelme_json = glob.glob( labelme_folder +'/*.json')
# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)