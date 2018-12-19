import glob
import csv

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

def readFile(file):
    collector = []
    with open(file) as infile:
        for line in infile:
            collector.append(removeUnwantedCharacter(line))
    return collector

def saveToCsvFile(collector, file):
    with open(file, mode='wt', newline='') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        writer.writerows(collector)

# Main

# list.cluster=none,p2p,level,hori
# list.algorithm=nsgaiii,ensgaiii

# F:\My_PhD_Works\Experiments\journal01\output

source_dir = 'F:/My_PhD_Works/Experiments/journal01/output/*/*a5_indicator.out'

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