import glob
import csv
import shutil
import os

from a3_normalizer import A3Normalizer

#######################################################

def getWindowDirectory():
    # pwangsom, Peerasak
    window_user = ['pwangsom', 'Peerasak']

    dest_dir = 'D:/Users/' + window_user[0] + '/Google Drive KMUTT/PhD Works'

    if(os.path.exists(dest_dir) == False):
        dest_dir = 'D:/Users/' + window_user[1] + '/Google Drive KMUTT/PhD Works'

    return dest_dir

#######################################################

def saveToCsvFile(collector, file):
    with open(file, mode='wt', newline='') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        writer.writerows(collector)

#######################################################

def normalizedEachFile(file):

    workflow_lines = []

    with open(file) as inFile:
        for line in inFile:
            fields = line.replace('\n','').replace('\r', '').split(',')
            
            _line = [fields[0], int(fields[1]), fields[2], fields[3], int(fields[4]), int(fields[5]), \
            float(fields[7]), float(fields[8]), float(fields[9]), 0.0, 0.0, 0.0]
            
            workflow_lines.append(_line)

    normalizer = A3Normalizer()
    normalizer.workflow_lines = workflow_lines
    
    workflow_lines = normalizer.normalize()

    return workflow_lines

#######################################################

def readA3File(file_list):

    i = 1

    print("Files in list: \t\t\t" + str(len(file_list)) + " files")

    for file_item in file_list:
        file = file_item[2].replace('\\', '/')
        print(str(i) + " " + file)

        workflow_lines = normalizedEachFile(file)
        dest_file = file.replace('a3_lastgen_objective.csv', 'a3_normalized_objective.csv')

        saveToCsvFile(workflow_lines, dest_file)
        print(dest_file)

        i += 1    

#######################################################

def sortFiles(source_dir):

    print(source_dir)
    out_files = glob.glob(source_dir)
    file_list = []
    i = 1

    print("Files in source folder: \t" + str(len(out_files)) + " files")
    print("")

    for file in out_files:
        file = file.replace('\\', '/')

        file_name = file.rsplit('/', 1)[1].split('_')

        workflow_name = file_name[0]
        workflow_size = file_name[1]

        current_file = [workflow_name, workflow_size, file]

        file_list.append(current_file)

        i += 1

    file_list = sorted(file_list, key=lambda x: (x[0], int(x[1])))

    return file_list

#######################################################
#######################################################

# Main

experiment = 'pilot01'

main_source = getWindowDirectory() + '/Experiments/'+ experiment + '/output/'
source_dir = main_source + '*a3_lastgen_objective.csv'

file_list = sortFiles(source_dir)
readA3File(file_list)

#######################################################