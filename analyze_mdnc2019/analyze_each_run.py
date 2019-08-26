import glob
import csv
import shutil
import os
import operator

#######################################################

def getWindowDirectory():
    # pwangsom, Peerasak
    window_user = ['pwangsom', 'Peerasak']

    window_dir = 'D:/Users/' + window_user[0] + '/Google Drive KMUTT/PhD Works'

    if(os.path.exists(window_dir) == False):
        window_dir = 'D:/Users/' + window_user[1] + '/Google Drive KMUTT/PhD Works'

    return window_dir

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

def getAverageOfSpecificedLine(file, algorithm, cluster, maxrun, maxgen, replicate, mode):
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


    if (len(collector) > 0):
        if(mode == 0):
            collector.sort(key = operator.itemgetter(4))
        elif(mode == -1):
            collector.sort(key = operator.itemgetter(7))
        elif(mode == 1):
            collector.sort(key = operator.itemgetter(7), reverse=True)

        collector = collector[:replicate]
        value = getAverageValue(collector)

    return value  

#######################################################

def readFile(source_dir, file_list, algorithms, clusters, maxrun, maxgen, replicate):

    i = 1
    for file in file_list:
        print(str(i) + " " + file[0])

        for algo in algorithms:
            #print(str(i) + " " + file[0] + " " + algo)

            for cluster in clusters:
                #print(str(i) + " " + file[0] + " " + algo + " " + cluster)
                print(getAverageOfSpecificedLine(file[0], algo, cluster[0], maxrun, maxgen, replicate, cluster[1]))

        i += 1


    print("")

#######################################################

maxgen = 300
maxrun = 30
replicate = 24
worlflow_size = 'cybershake_500'

algorithms = ['nsgaiii', 'ensgaiii']
clusters = [['none', -1], ['p2p', 0], ['level', 1]]

experiment = 'MDNC2019/max30runs'

source_dir = getWindowDirectory() + '/Experiments/'+ experiment + '/experiment0/output/' + worlflow_size + '_a5_indicator.csv'

file_list = listAndSortFiles(source_dir)

readFile(source_dir, file_list, algorithms, clusters, maxrun, maxgen, replicate)
