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

def accomulateAllInputs(dest_dir):

    source_dir = dest_dir + "*/experiment0/output/*a5_lastgen_indicator.csv"

    print(source_dir)
    out_files = glob.glob(source_dir)

    i = 1

    print("Files in list: " + str(len(out_files)) + " files")

    all_collector = []
    content_collector = []

    for file in out_files:
        file = file.replace('\\', '/')
        print(str(i) + " " + file)

        with open(file) as infile:
            line_no = 1

            for line in infile:
                if(line_no == 1):
                    if(i == 1):
                        fields = line.replace('\n','').replace('\r', '').split(',')
                        all_collector.append(fields)
                else:
                   fields = line.replace('\n','').replace('\r', '').split(',')
                   content_collector.append(fields)
                
                line_no += 1

        i += 1

    content_collector = sorted(content_collector, key=lambda x: (x[0], int(x[1]), x[2], int(x[4])))
    all_collector = all_collector + content_collector

    dest_dir = dest_dir + 'analyze/all_input_a5_lastgen_indicator.csv'

    saveToCsvFile(all_collector, dest_dir)


#######################################################
#######################################################

# Main

experiment = 'multipleinput'

# source_dir = 'F:/My_PhD_Works/Experiments/' + experiment + '/output/*/*a3_objective.out'
main_source = 'F:/My_PhD_Works/Experiments/' + experiment + '/*/output/*/'

dest_dir = getWindowDirectory() + '/Experiments/'+ experiment + '/'

# Step 1. convert a5.out to a5.csv
#source_dir = main_source + '*a5_indicator.out'
#convertOutToCsv(source_dir)

# Step 2. extract last gen from a5.csv
#source_dir = main_source + '*a5_indicator.csv'
#extractLastGenFromCsv(source_dir, dest_dir)

# Step 3. accumolate all inputs
accomulateAllInputs(dest_dir)

#######################################################