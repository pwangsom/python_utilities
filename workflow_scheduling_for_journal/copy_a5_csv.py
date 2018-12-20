import glob
import shutil

# Main

# F:\My_PhD_Works\Experiments\journal01\output
# D:\Users\Peerasak\Google Drive KMUTT\PhD Works\Experiments\journal\journal01\output

experiment = 'journal03'

source_dir = 'F:/My_PhD_Works/Experiments/' + experiment + '/output/*/*a5_indicator.csv'
dest_dir = 'D:/Users/Peerasak/Google Drive KMUTT/PhD Works/Experiments/journal/' + experiment + '/output/'

out_files = glob.glob(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

i = 1

for file in out_files:
    file = file.replace('\\', '/')
    print(str(i) + " " + file)

    new_file_name = file.rsplit('/', 1)[1]

    new_file = dest_dir + new_file_name
    shutil.copy(file, new_file)

    print(str(i) + " " + new_file)
    print("")
    
    i += 1