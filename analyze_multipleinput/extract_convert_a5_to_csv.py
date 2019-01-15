import glob
import csv
import shutil
import os

#######################################################

def removeUnwantedCharacter(line):

    line = line.replace("_runALL", "_run98")
    line = line.replace("_runAvgALL", "_run99")
    line = line.replace("_maxgen300_genLAST", "_maxgen300_gen300")
    line = line.replace("_maxgen600_genLAST", "_maxgen600_gen600")
    line = line.replace("_maxgen900_genLAST", "_maxgen900_gen900")
    line = line.replace("_maxgenALL_genLAST", "_maxgen999_gen999")
    
    line = line.replace("_run", "_")
    line = line.replace("_maxgen", "_")
    line = line.replace("_gen", "_")
    
    line = line.replace(", ", ",")[:-2]
    line = line.replace("_", ",").lower()
    
    return line.split(',')

#######################################################

def readFile(file, mode):
    collector = []

    i = 1

    with open(file) as infile:
        for line in infile:
            if(mode == 1):
                collector.append(removeUnwantedCharacter(line))
            elif(mode == 2):
                if(i == 1):
                    fields = line.replace('\n','').replace('\r', '').split(',')
                    collector.append(fields)
                else:
                    skip = [98, 99]
                    fields = line.replace('\n','').replace('\r', '').split(',')
                    if(int(fields[5]) == int(fields[6]) and int(fields[4]) not in skip):
                        collector.append(fields)
            
            i = i+1

    return collector

#######################################################

def saveToCsvFile(collector, file):
    with open(file, mode='wt', newline='\n') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        writer.writerows(collector)

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

        saveToCsvFile(readFile(file, 1), saveAsFile)

        print(str(i) + " " + saveAsFile)
        print("")

        i += 1

#######################################################

def extractLastGenFromCsv(source_dir, dest_dir):

    print(source_dir)
    out_files = glob.glob(source_dir)

    i = 1

    print("Files in list: " + str(len(out_files)) + " files")

    for file in out_files:
        file = file.replace('\\', '/')
        print(str(i) + " " + file)

        split_file_name = file.rsplit('/', 4)

        saveAsFile = dest_dir + split_file_name[1] + "/experiment0/output/" + split_file_name[4]
        saveAsFile = saveAsFile.replace('a5_indicator', 'a5_lastgen_indicator')

        saveToCsvFile(readFile(file, 2), saveAsFile)

        print(str(i) + " " + saveAsFile)
        print("")

        i += 1

#######################################################
#######################################################

# Main

experiment = 'multipleinput'

# source_dir = 'F:/My_PhD_Works/Experiments/' + experiment + '/output/*/*a3_objective.out'
main_source = 'F:/My_PhD_Works/Experiments/' + experiment + '/*/output/*/'

dest_dir = getWindowDirectory() + '/Experiments/'+ experiment + '/'

# Step 1. convert a3.out to a3.csv
source_dir = main_source + '*a5_indicator.out'
convertOutToCsv(source_dir)

# Step 2. extract last gen from a3.csv
source_dir = main_source + '*a5_indicator.csv'
extractLastGenFromCsv(source_dir, dest_dir)

#######################################################