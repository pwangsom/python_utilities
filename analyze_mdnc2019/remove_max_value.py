import glob
import csv
import shutil
import os
import operator

#######################################################

def getAverageValue(data):

    size = len(data)
    i = 0.0
    for item in data:
        i += float(item[7])

    average = data[0]
    average[4] = average[5]
    average[7] = i / size

    return average  

#######################################################

def readFile(file, algorithm, cluster, maxrun, maxgen, n_remove, mode):
    print(file)
    collector = []
    value = []
    with open(file) as infile:
        i = 1
        for line in infile:
            fields = line.replace('\n','').replace('\r', '').split(',')
            if (i != 1 and fields[2] == cluster and fields[3] == algorithm and int(fields[4]) <= maxrun and int(fields[5]) == maxgen and int(fields[5]) == int(fields[6])):
                row = [fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[8]]
                collector.append(row)
            i += 1

    if (len(collector) > 0 and n_remove > 0):
        collector.sort(key = operator.itemgetter(7), reverse=mode)
        collector = collector[:maxrun - n_remove]
        
    value = getAverageValue(collector)

    print(value)

#######################################################            

maxgen = 300
maxrun = 30

n_remove = 4
worlflow_size = 'epigenomics_100'
mode = False

algorithm = 'ensgaiii'
cluster = 'p2p'

experiment = 'MDNC2019/max30runs'

file_name = 'D:/Users/pwangsom/Google Drive KMUTT/PhD Works/Experiments/'+ experiment + '/experiment0/output/' + worlflow_size + '_a5_indicator.csv'

readFile(file_name, algorithm, cluster, maxrun, maxgen, n_remove, mode)