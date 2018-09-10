import glob
import shutil

# Main

#E:\My_PhD_Works\Experiments\icmla02300\output\*\*_runALL_maxgen300_genLAST_all_normalized_objective.out

source_dir = 'E:/My_PhD_Works/Experiments/icmla02300/output/*/*_runALL_maxgen300_genLAST_all_normalized_objective.out'
dest_dir = 'D:/Users/Peerasak/git/matlab-works/plot-3-objectives/icmla02300/'

out_files = glob.glob(source_dir)

print("Files in list: " + str(len(out_files)) + " files")

for file in out_files:
    file = file.replace('\\', '/')
    print(file)

    file_name = file.rsplit('/', 1)[1]

    new_file_name = file_name.rsplit('_', 6)[0] + '.out'

    new_file = dest_dir + new_file_name
    print(new_file)

    shutil.copy(file, new_file)
