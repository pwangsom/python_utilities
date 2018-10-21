import glob
import csv

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

def writeValueToFile(collector, file):
    with open(file, mode='wt', encoding='utf-8', newline='') as myfile:
        writer = csv.writer(myfile)
        writer.writerows(collector)

def avgL(l):
    return sum(l) / float(len(l))

# Main

source_dir = 'D:/opt/Experiment/ola011/experiment0/output/*/*1000*_a5_indicator.out'
dest_dir = 'D:/opt/Experiment/ola011/experiment0/analyze/1000_a5_indicator_summary.out'

size = 1000
a1 = 'ensga_iii'
a2 = 'nsga_iii'
a3 = 'nsga_ii'

out_files = glob.glob(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

globalCollector = []
globalReport = []

ensgaiii_pareto = []
nsgaiii_pareto = []
nsgaii_pareto = []

ensgaiii_hv = []
nsgaiii_hv = []
nsgaii_hv = []

ensgaiii_igd = []
nsgaiii_igd = []
nsgaii_igd = []

for file in out_files:
    file = file.replace('\\', '/')
    print(file)

    globalCollector.extend(getSpecificedLine(file))

for line in globalCollector:
    values = line.split(',')

    if(values[2] == 'ensgaiii'):
        ensgaiii_pareto.append(float(values[6]))
        ensgaiii_hv.append(float(values[7]))
        ensgaiii_igd.append(float(values[13]))
    elif(values[2] == 'nsgaiii'):
        nsgaiii_pareto.append(float(values[6]))
        nsgaiii_hv.append(float(values[7]))
        nsgaiii_igd.append(float(values[13]))
    elif(values[2] == 'nsgaii'):
        nsgaii_pareto.append(float(values[6]))
        nsgaii_hv.append(float(values[7]))
        nsgaii_igd.append(float(values[13]))

""" print(ensgaiii_pareto)
print(ensgaiii_hv)
print(ensgaiii_igd)

print(sum(ensgaiii_pareto) / float(len(ensgaiii_pareto)))
print(sum(ensgaiii_hv) / float(len(ensgaiii_hv)))
print(sum(ensgaiii_igd) / float(len(ensgaiii_igd))) """

globalReport.append([size, a1, avgL(ensgaiii_pareto), avgL(ensgaiii_hv), avgL(ensgaiii_igd)])
globalReport.append([size, a2, avgL(nsgaiii_pareto), avgL(nsgaiii_hv), avgL(nsgaiii_igd)])
globalReport.append([size, a3, avgL(nsgaii_pareto), avgL(nsgaii_hv), avgL(nsgaii_igd)])

writeValueToFile(globalReport, dest_dir)

print(globalReport)