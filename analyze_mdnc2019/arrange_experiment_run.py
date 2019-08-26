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

def readFile(file, algorithm, cluster, maxrun, maxgen, replicate, mode):
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

    if(mode == -30):
        collector.sort(key = operator.itemgetter(7))
    elif(mode == 1):
        collector.sort(key = operator.itemgetter(7), reverse=True)
    elif(mode < 0):
        collector.sort(key = operator.itemgetter(7))
        collector = collector[: maxrun + mode]
        collector.sort(key = operator.itemgetter(4))
    else:
        collector.sort(key = operator.itemgetter(4))
    
    collector = collector[:replicate]                
    value = getAverageValue(collector)

    print(value)

#######################################################  

maxgen = 300
maxrun = 30

replicate = 25
mode = -1

algorithm = 'ensgaiii'
cluster = 'p2p'

# cybershake_50, cybershake_100, cybershake_500, cybershake_800, cybershake_1000
# epigenomics_50, epigenomics_100, epigenomics_500, epigenomics_800, epigenomics_1000
# ligo_50, ligo_100, ligo_500, ligo_800, ligo_1000
# montage_50, montage_100, montage_500, montage_800, montage_1000
# sipht_50, sipht_100, sipht_500, sipht_800, sipht_1000

worlflow_size = 'montage_500'

experiment = 'MDNC2019/max30runs'
file_name = 'D:/Users/pwangsom/Google Drive KMUTT/PhD Works/Experiments/'+ experiment + '/experiment0/output/' + worlflow_size + '_a5_indicator.csv'

readFile(file_name, algorithm, cluster, maxrun, maxgen, replicate, mode)