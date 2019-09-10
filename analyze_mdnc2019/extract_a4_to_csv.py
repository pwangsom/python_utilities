import glob
import csv
import shutil
import os

#######################################################

def getWindowDirectory():
    # pwangsom, Peerasak
    window_user = ['pwangsom', 'Peerasak']

    window_dir = 'D:/Users/' + window_user[0] + '/Google Drive KMUTT/PhD Works'

    if(os.path.exists(window_dir) == False):
        window_dir = 'D:/Users/' + window_user[1] + '/Google Drive KMUTT/PhD Works'

    return window_dir

#######################################################

def convertOutToCsv(source_dir):

    print(source_dir)
    out_files = glob.glob(source_dir)

    i = 1

    print("Files in list: " + str(len(out_files)) + " files")

    for file in out_files:
        file = file.replace('\\', '/')
        print(str(i) + " " + file)

        saveAsFile = file.replace(".out", ".csv")

        saveToCsvFile(readFile(file), saveAsFile)

        print(str(i) + " " + saveAsFile)
        print("")

        i += 1

#######################################################

# Main

experiment = 'MDNC2019/max30runs'

main_source = 'D:/Users/pwangsom/Experiments/' + experiment + '/output/*/'

dest_dir = getWindowDirectory() + '/Experiments/'+ experiment + '/experiment0/output/'

# Step 1. convert a5.out to a5.csv
print("Step 1. convert a5.out to a5.csv")
source_dir = main_source + '*a5_indicator.out'
convertOutToCsv(source_dir)