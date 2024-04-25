import os
from sys import argv

def file_manager():
    """
    Usage: execute script with windows path as argument
    Supported Types: pdf, mp3, mp4, doc, docx, ppt, pptx, jpeg, png
    To add types, simply add them to file_folder_correlation
    """

    #list of supported types
    file_folder_correlation={
        ".pdf": "PDF",
        ".mp3": "Audio",
        ".mp4": "Video",
        ".doc": "Word",
        ".docx": "Word",
        ".ppt": "PowerPoint",
        ".pptx": "PowerPoint",
        ".jpeg": "Images",
        ".png": "Images",
        
    }

    path_to_manage = path_translation(argv[1])

    #loop through dir-content and supported file-types
    for elem in os.listdir(path_to_manage):
        for ending in file_folder_correlation.keys():

            #check for supported types
            if elem.endswith(ending):

                dest_folder = file_folder_correlation[ending]

                #create folder for file type if it doesn't exist
                if not f"{path_to_manage}/{dest_folder}" in os.listdir(path_to_manage):
                    os.mkdir(f"{path_to_manage}/{dest_folder}")

                #move file
                os.rename(f"{path_to_manage}/{elem}", f"{path_to_manage}/{dest_folder}/{elem}")

    #confirm success
    print("Sorting succesfully finished")


def path_translation(path):
    #bring windows path in linux syntax
    path= path.replace("\\", "/").replace(":", "")
    path = path[0].lower() + path[1:]
    new_path = f"/mnt/{path}"
    return new_path



file_manager()