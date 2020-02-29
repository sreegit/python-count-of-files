import os
from config import *
# import pathlib

def getListofDirectories(dirName):
    print("#### Result ####")

    dirListing = os.listdir(dirName)

    print("Number of Directories: ")
    print(len(dirListing))


# dirPath = "/media/sks/All-Data/git-pinpark/plate-recognition-all-proj/sreerag"

getListofDirectories(dirPath)


def getCount(thePath):
    cpt = sum([len(files) for r, d, files in os.walk(thePath)])
    print("Number of files: ")
    print(cpt)

getCount(dirPath)