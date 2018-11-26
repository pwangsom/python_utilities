import glob

def readFile(file):
    collector = []
    with open(file) as infile:
        for line in infile:
            collector.append(line[:-3])
    return collector 

def convertTupleToSet(tuples):
    aSet = set()
    for t in tuples:
        aSet.add(t)

    return aSet

def writeSummaryToFile(collector, file):
    with open(file, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(collector))

# Main

# E:\My_PhD_Works\Experiments
# D:\Users\Peerasak\Google Drive KMUTT\PhD Works\Experiments\OLA2019\ola01\analyze
# 'E:/My_PhD_Works/Experiments/ola05' + size + '/output/*/*' + size + '*_runALL_maxgenALL_genLast_normalized_pareto.out'

size = '250'

source_dir = 'F:/My_PhD_Works/Experiments/ola060500/output/*_' + size + '*/*' + size + '*_runALL_maxgenALL_genLast_normalized_pareto.out'

print(source_dir)

out_files = glob.glob(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

count = 1

for file in out_files:
    file = file.replace('\\', '/')
    print(str(count) + ": " + file)
    count += 1

    collector = []
    collector.extend(readFile(file))
    t = tuple(collector)
    old = len(t)

    aSet = convertTupleToSet(t)

    print(str(old) + " -> " + str(len(aSet)))

    newFile = file.replace("_runALL_maxgenALL_", "_distinct_")

    writeSummaryToFile(aSet, newFile)