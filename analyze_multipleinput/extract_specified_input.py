import glob
import csv
import shutil
import os

""" check_list = [
    ['cybershake', '50', 'input04'],
    ['cybershake', '100', 'input18'],
    ['cybershake', '500', 'input02'],
    ['cybershake', '800', 'input01'],
    ['cybershake', '1000', 'input01'],
    ['epigenomics', '50', 'input01'],
    ['epigenomics', '100', 'input05'],
    ['epigenomics', '500', 'input01'],
    ['epigenomics', '800', 'input02'],
    ['epigenomics', '1000', 'input01'],
    ['ligo', '50', 'input01'],
    ['ligo', '100', 'input01'],
    ['ligo', '500', 'input01'],
    ['ligo', '800', 'input05'],
    ['ligo', '1000', 'input01'],
    ['montage', '50', 'input01'],
    ['montage', '100', 'input01'],
    ['montage', '500', 'input06'],
    ['montage', '800', 'input09'],
    ['montage', '1000', 'input11'],
    ['sipht', '50', 'input08'],
    ['sipht', '100', 'input08'],
    ['sipht', '500', 'input08'],
    ['sipht', '800', 'input13'],
    ['sipht', '1000', 'input08'],
] """

check_list = [
    ['cybershake', '50', 'input03'],
    ['cybershake', '100', 'input18'],
    ['cybershake', '500', 'input04'],
    ['cybershake', '800', 'input02'],
    ['cybershake', '1000', 'input06'],
    ['epigenomics', '50', 'input02'],
    ['epigenomics', '100', 'input01'],
    ['epigenomics', '500', 'input07'],
    ['epigenomics', '800', 'input01'],
    ['epigenomics', '1000', 'input06'],
    ['ligo', '50', 'input03'],
    ['ligo', '100', 'input11'],
    ['ligo', '500', 'input02'],
    ['ligo', '800', 'input09'],
    ['ligo', '1000', 'input02'],
    ['montage', '50', 'input03'],
    ['montage', '100', 'input03'],
    ['montage', '500', 'input02'],
    ['montage', '800', 'input03'],
    ['montage', '1000', 'input01'],
    ['sipht', '50', 'input05'],
    ['sipht', '100', 'input05'],
    ['sipht', '500', 'input05'],
    ['sipht', '800', 'input01'],
    ['sipht', '1000', 'input04'],

]

def saveToCsvFile(collector, file):
    with open(file, mode='wt', newline='\n') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        writer.writerows(collector)


def isNeedLine(fields):
    i = 0
    n = 0

    while i == 0 and n < len(check_list):
        if(fields == check_list[n]):
            i = n + 1
            print("found in " + str(i))
        
        n += 1
    return i

# Main


# D:\Users\pwangsom\Google Drive KMUTT\PhD Works\Experiments\multipleinput\analyze
source_dir = 'D:/Users/pwangsom/Google Drive KMUTT/PhD Works/Experiments/multipleinput/analyze/multipleinput_a5_lastgen_indicator.csv'

out_files = glob.glob(source_dir)
i = 1

for file in out_files:
    file = file.replace('\\', '/')
    print(str(i) + " " + file)

    with open(file) as infile:

        all_collector = []
        content_collector = []
        line_no = 1
        
        for line in infile:
            if(line_no == 1):
                fields = line.replace('\n', '').replace('\r', '').split(',')
                all_collector.append(fields)
            else:
                fields = line.replace('\n', '').replace('\r', '').split(',')
                found = isNeedLine([fields[0], fields[1], fields[21]])
                if(found > 0):
                    content_collector.append(fields)
            
            line_no += 1
    
        all_collector = all_collector + content_collector

        dest_dir = source_dir.replace('multipleinput_a5_lastgen_indicator.csv', 'multipleinput_a5_lastgen_single_indicator.csv')
        saveToCsvFile(all_collector, dest_dir)