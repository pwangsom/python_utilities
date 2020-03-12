import glob
import csv

globalLines = set()
globalCollector = []

def removeUnwantedCharacter(line):
    line = line.replace("_runAvgALL", "_run99")    
    line = line.replace("_run", "_")
    line = line.replace("_maxgen", "_")
    line = line.replace("_gen", "_")
    
    line = line.replace(", ", ",")[:-1]
    line = line.replace("_", ",").lower()
    values = line.split(',')
    string = values[6] + "," + values[7] + "," + values[8]
    ls = [values[6], values[7], values[8]]
    
    return [string, ls]

def getSpecificedLine(file, algorithm):
    con1 = "_" + algorithm
    con2 = "_gen300"
    with open(file) as infile:
        for line in infile:
            if (line.find(con1) != -1):
                if(line.find(con2) != -1):
                    [wantedLine, listLine] = removeUnwantedCharacter(line)
                    if wantedLine not in globalLines:
                        globalLines.add(wantedLine)
                        globalCollector.append(listLine)


def writeValueToFile(collector, file):
    with open(file, mode='wt', encoding='utf-8', newline='') as myfile:
        writer = csv.writer(myfile)
        writer.writerows(collector)


def run(algorithm, size):
    
    globalLines.clear()
    globalCollector.clear()

    insId = '_all'
    #size = '750'
    #algorithm = 'nsgaii'
    #algorithm = 'nsgaiii'
    #algorithm = 'ensgaiii'
    run = 'runALL'

    source_dir = 'D:/opt/Experiment/ola01/experiment0/output/*/*' + size + '*_a4_normalized_objective.out'
    dest_dir = 'D:/Users/Peerasak/git/matlab-works/plot-3-objectives/ola01/out/'

    print(source_dir)

    out_files = glob.glob(source_dir)

    print("Files in list: " + str(len(out_files)) + " files")

    for file in out_files:
        file = file.replace('\\', '/')
        print(file)

        old_size = len(globalCollector)
        getSpecificedLine(file, algorithm)
        new_size = len(globalCollector)

        print("old_size: " + str(old_size) + ", new_size: + " + str(new_size))


    new_file = dest_dir + size + insId + '_' + run + '_' + algorithm + '.out'
    print(new_file)

    writeValueToFile(globalCollector, new_file)

size = '500'

algorithms = ['nsgaii', 'nsgaiii', 'ensgaiii']

for a in algorithms:
    run(a, size)
