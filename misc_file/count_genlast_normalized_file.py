import glob

def readFile(file):
    with open(file) as infile:
        for i, l in enumerate(infile):
            pass
    return i + 1 

def avg(l):
    return sum(l) / float(len(l))

# Main

size = '1000'

source_dir = 'E:/My_PhD_Works/Experiments/ola05' + size + '/output/*/*' + size[2:] + '*_distinct_genLast_normalized_pareto.out'

print(source_dir)

out_files = glob.glob(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

count = 1

ensgaiii = []
nsgaiii = []
nsgaii = []

for file in out_files:
    file = file.replace('\\', '/')
    print(str(count) + ": " + file)
    count += 1

    algo = file.split("/")[-1].split("_")[3]

    if (algo == "ensgaiii"):
        ensgaiii.append(readFile(file))
    elif(algo == "nsgaiii"):
        nsgaiii.append(readFile(file))
    elif(algo == "nsgaii"):
        nsgaii.append(readFile(file))

print("")
print("===ALL===")
print(nsgaii)
print(nsgaiii)
print(ensgaiii)

print("")
print(str(min(nsgaii)) + "," + str(max(nsgaii)) + "," + str(avg(nsgaii)))
print(str(min(nsgaiii)) + "," + str(max(nsgaiii)) + "," + str(avg(nsgaiii)))
print(str(min(ensgaiii)) + "," + str(max(ensgaiii)) + "," + str(avg(ensgaiii)))