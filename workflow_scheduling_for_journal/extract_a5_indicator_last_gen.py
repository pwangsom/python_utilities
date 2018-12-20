import glob
import csv

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
    print(str(i) + " " + file)

    file_name = file.rsplit('/', 1)[1].split('_')

    workflow_name = file_name[0]
    workflow_size = file_name[1]

    current_file = [file, workflow_name, workflow_size]

    file_list.append(current_file)

    i += 1

file_list = sorted(file_list, key=lambda x: (x[1], int(x[2])))

print("")

i = 1
for file in file_list:
    print(str(i) + " " + file[0])
    i += 1