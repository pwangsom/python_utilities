import glob
import csv

def getSpecificedLine(file):
    collector = []
    with open(file) as infile:
        i = 1
        for line in infile:
            fields = line.replace('\n','').replace('\r', '').split(',')
            if (i != 1 and int(fields[5]) == int(fields[6])) :
                collector.append(fields)
                # print(fields)
                # print(collector)
            i += 1

    collector = sorted(collector, key=lambda x: (x[2], x[3]))

    return collector    

def saveToCsvFile(collector, file):
    with open(file, mode='wt', newline='') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        writer.writerows(collector)

# Main

# D:\Users\Peerasak\Google Drive KMUTT\PhD Works\Experiments\journal\journal01\output

# pwangsom, Peerasak
window_user = 'pwangsom'
experiment = 'journal01'

source_dir = 'D:/Users/' + window_user + '/Google Drive KMUTT/PhD Works/Experiments/journal/' + experiment + '/output/*a5_indicator.csv'

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

print("")

content = []

i = 1
for file in file_list:
    print(str(i) + " " + file[0])

    if(i == 1):
        with open(file[0], 'r') as f:
            head = f.readline().replace('\n','').replace('\r', '')
            head = head.split(',')
            # print(head)

            content.append(head)

        content.extend(getSpecificedLine(file[0]))
    else:
        content.extend(getSpecificedLine(file[0]))

    #print(content)

    i += 1


saveAsFile = source_dir.replace('\\', '/')
saveAsFile = saveAsFile.rsplit('/', 1)[0]
saveAsFile = saveAsFile + '/' + experiment + '_a5_indicator_all.csv'

print(saveAsFile)

saveToCsvFile(content, saveAsFile)