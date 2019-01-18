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

def readFile(file):
    collector = []
    with open(file) as infile:
        for line in infile:
            collector.append(removeUnwantedCharacter(line))
    return collector

#######################################################

def saveToCsvFile(collector, file):
    with open(file, mode='wt') as myfile:
        writer = csv.writer(myfile, lineterminator='\n')
        writer.writerows(collector)

#######################################################

def getSpecificedLine(file, types, maxgen):
    collector = []
    with open(file) as infile:
        i = 1
        for line in infile:
            fields = line.replace('\n','').replace('\r', '').split(',')
            if (i != 1 and int(fields[4]) == types and int(fields[5]) == maxgen and int(fields[5]) == int(fields[6])) :
                collector.append(fields)
            i += 1

    collector = sorted(collector, key=lambda x: (x[2], x[3]))

    return collector  

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

def copyFile(source_dir, dest_dir):

    print(source_dir)
    out_files = glob.glob(source_dir)
    print("Files in list: " + str(len(out_files)) + " files")

    i = 1

    for file in out_files:
        file = file.replace('\\', '/')
        print(str(i) + " " + file)

        new_file_name = file.rsplit('/', 1)[1]

        new_file = dest_dir + new_file_name
        shutil.copy(file, new_file)

        print(str(i) + " " + new_file)
        print("")
        
        i += 1

#######################################################

def listAndSortFiles(source_dir):
    print(source_dir)
    out_files = glob.glob(source_dir)
    i = 1

    print("Files in list: " + str(len(out_files)) + " files")

    file_list = []

    for file in out_files:
        file = file.replace('\\', '/')
        # print(str(i) + " " + file)

        file_name = file.rsplit('/', 1)[1].split('_')

        workflow_name = file_name[0]
        workflow_size = file_name[1]

        current_file = [file, workflow_name, workflow_size]

        file_list.append(current_file)

        i += 1

    file_list = sorted(file_list, key=lambda x: (x[1], int(x[2])))

    return file_list

#######################################################

def generateSummaryFile(source_dir, file_list, types, maxgen):
    content = []

    i = 1
    for file in file_list:
        print(str(i) + " " + file[0])

        if(i == 1):
            with open(file[0], 'r') as f:
                head = f.readline().replace('\n','').replace('\r', '')
                head = head.split(',')

                content.append(head)

            content.extend(getSpecificedLine(file[0], types, maxgen))
        else:
            content.extend(getSpecificedLine(file[0], types, maxgen))

        i += 1


    file_type = types == 99 and 'average' or 'archive'

    saveAsFile = source_dir.replace('\\', '/')
    saveAsFile = saveAsFile.rsplit('/', 4)[0]
    saveAsFile = saveAsFile + '/level_a5_indicator_' + file_type + '.csv'

    print(saveAsFile)

    saveToCsvFile(content, saveAsFile)

    print("")

#######################################################
#######################################################

# Main

experiment = 'specifiedinput/level'

# source_dir = 'F:/My_PhD_Works/Experiments/' + experiment + '/output/*/*a3_objective.out'
main_source = 'F:/My_PhD_Works/Experiments/' + experiment + '/output/*/'

dest_dir = getWindowDirectory() + '/Experiments/'+ experiment + '/experiment0/output/'

# Step 1. convert a5.out to a5.csv
print("Step 1. convert a5.out to a5.csv")
source_dir = main_source + '*a5_indicator.out'
convertOutToCsv(source_dir)

# Step 2. copy a5.csv
print("Step 2. copy a5.csv")
source_dir = main_source + '*a5_indicator.csv'
copyFile(source_dir, dest_dir)

# Step 3. list all file for preparation to generate summary file
print("Step 3. list all file for preparation to generate summary file")
source_dir = dest_dir + '*a5_indicator.csv'
file_list = listAndSortFiles(source_dir)

# Step 4. generate archive summary file
print("Step 4. generate archive summary file")
generateSummaryFile(source_dir, file_list, 98, 300)

# Step 5. generate average summary file
print("Step 5. generate average summary file")
generateSummaryFile(source_dir, file_list, 99, 300)

#######################################################