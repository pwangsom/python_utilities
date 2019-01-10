import glob
import os

def copyPerpertiesFile(main_source, main_dest, max_instance):

    out_files = glob.glob(main_source + '/*.properties')

    for file in out_files:

        file = file.replace('\\', '/')
        file_name = file.rsplit('/', 1)[1]

        for i in range(max_instance):
            dir_id = format(i+1, '02')
            dest_file = main_dest + 'input' + dir_id + '/' + file_name


            f = open(file, "r")
            copy = open(dest_file, 'w', newline='\n')

            for line in f:
                line = line.replace("multiple_00", "multiple_" + dir_id)                
                line = line.replace("/multipleinput/input00", "/multipleinput/input" + dir_id)
                copy.write(line)

            f.close()
            copy.close()
        
    return

#######################################################

def copyShFile(main_source, main_dest, max_instance):

    out_files = glob.glob(main_source + '/*.sh')

    for file in out_files:

        file = file.replace('\\', '/')
        file_name = file.rsplit('/', 1)[1]

        for i in range(max_instance):
            dir_id = format(i+1, '02')
            dest_file = main_dest + 'input' + dir_id + '/' + file_name


            f = open(file, "r")
            copy = open(dest_file, 'w', newline='\n')

            for line in f:             
                line = line.replace("/multipleinput/input00", "/multipleinput/input" + dir_id)
                copy.write(line)

            f.close()
            copy.close()
        
    return

#######################################################

# Main

# F:\My_PhD_Works\Pegasus_Input\SyntheticWorkflows
main_source = 'D:/Users/pwangsom/Google Drive KMUTT/PhD Works/Experiments/multipleinput/slurm'

# D:\Users\pwangsom\Google Drive KMUTT\PhD Works\Experiments\pegasus_input
main_dest = 'D:/Users/pwangsom/Google Drive KMUTT/PhD Works/Experiments/multipleinput/'

max_instance = 20

copyPerpertiesFile(main_source, main_dest, max_instance)

copyShFile(main_source, main_dest, max_instance)