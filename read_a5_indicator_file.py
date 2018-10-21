import glob

def removeUnwantedCharacter(line):
    line = line.replace("_runAvgALL", "_run99")    
    line = line.replace("_run", "_")
    line = line.replace("_maxgen", "_")
    line = line.replace("_gen", "_")
    
    line = line.replace(", ", ",")[:-1]
    
    return line.replace("_", ",").lower()

def getSpecificedLine(file):
    collector = []
    with open(file) as infile:
        for line in infile:
            if (line.find("_runAvgALL_maxgen300_gen300") != -1):
                collector.append(removeUnwantedCharacter(line))
    return collector        

def writeSummaryToFile(collector, file):
    with open(file, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(collector))

# Main

source_dir = 'D:/opt/Experiment/ola011/experiment0/output/*/*1000*_a5_indicator.out'
dest_dir = 'D:/opt/Experiment/ola011/experiment0/analyze/1000_a5_indicator.out'

out_files = glob.glob(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

globalCollector = []

for file in out_files:
    file = file.replace('\\', '/')
    print(file)

    globalCollector.extend(getSpecificedLine(file))

writeSummaryToFile(globalCollector, dest_dir)

