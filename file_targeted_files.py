import glob

# Main

size = '1000'

source_dir = 'F:/My_PhD_Works/Experiments/ola06*' + size + '/output/*_' + size + '*/'+ size + '*_a5_indicator.out'

out_files = glob.glob(source_dir)

print(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

for file in out_files:
    file = file.replace('\\', '/')
    print(file)