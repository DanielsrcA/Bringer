import os
import shutil

From="C:/Users/danie/Downloads/"
To="HOMEWORK ORGANIZER FOLDER/"

List= os.listdir(From)
for i in List:
    name,extension = os.path.splitext(i)
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1 = From + i
        path2 = To + "downloads/"
        path3 = To + "downloads/" + i

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)