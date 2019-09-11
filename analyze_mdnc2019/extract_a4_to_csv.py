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

def saveToCsvFile(collector, file):
    with open(file, mode='wt') as myfile:
        writer = csv.writer(myfile, lineterminator='\n')
        writer.writerows(collector)

#######################################################

def convertOutToCsv(source_dir, dest_dir):

    print(source_dir)
    out_files = glob.glob(source_dir)

    i = 1

    print("Files in list: " + str(len(out_files)) + " files")

    for file in out_files:
        file = file.replace('\\', '/')
        print(str(i) + " " + file)

        new_file_name = file.rsplit('/', 1)[1]
        new_file_name = new_file_name.replace("runALL_maxgen300_genLAST_all_normalized_objective.out", "archive.csv")
        
        new_file = dest_dir + new_file_name

        collector = []

        with open(file) as infile:
            for line in infile:
                line = line.replace(", ", ",")[:-2]
                collector.append(line.split(','))

        saveToCsvFile(collector, new_file)

        print(str(i) + " " + new_file)
        print("")

        i += 1

#######################################################

# Main

experiment = 'MDNC2019/max30runs'

main_source = 'D:/Users/pwangsom/Experiments/' + experiment + '/output/*/'

dest_dir = getWindowDirectory() + '/Experiments/'+ experiment + '/experiment0/output/archive/'

# Step 1. convert a5.out to a5.csv
print("Step 1. convert a5.out to a5.csv")
source_dir = main_source + '*runALL_maxgen300_genLAST_all_normalized_objective.out'
convertOutToCsv(source_dir, dest_dir)