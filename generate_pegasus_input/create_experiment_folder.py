import glob
import shutil
import os

# Main

# F:\My_PhD_Works\Pegasus_Input\SyntheticWorkflows
main_source = 'F:/My_PhD_Works/Pegasus_Input/SyntheticWorkflows/'

# D:\Users\pwangsom\Google Drive KMUTT\PhD Works\Experiments\pegasus_input
main_dest = 'D:/Users/pwangsom/Google Drive KMUTT/PhD Works/Experiments/multipleinput/'

workflow_list = [['CYBERSHAKE', 'cybershake'], ['GENOME', 'epigenomics'], ['LIGO','ligo'], ['MONTAGE', 'montage'], ['SIPHT', 'sipht']]
size_list = ['50', '100', '500', '800', '1000']
max_instance = 20

n = 1

for i in range(max_instance):

    dir_id = format(i+1, '02')
    dest_dir = main_dest + 'input' + dir_id + '/'

    exp_dir = dest_dir + 'experiment0/'
    input_dir = exp_dir + 'input/'
    output_dir = exp_dir + 'output/'
    log_dir = exp_dir + 'log/'

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        os.makedirs(exp_dir)
        os.makedirs(input_dir)
        os.makedirs(output_dir)
        os.makedirs(log_dir)

    for workflow in workflow_list:
        source_dir = main_source + workflow[0]

        for j in size_list:
            file_filter = source_dir + '/' + workflow[0] + '*.' + j + '.' + str(i) + '.dax'
            out_files = glob.glob(file_filter)

            dest_file = input_dir + workflow[1] + "_" + j + ".xml"

            shutil.copy(out_files[0], dest_file)

            print(str(n) + " : " + dest_file)

            n = n+1


