'''
This script can be used to combine the hla report that are generated from hla-typing pipeline.
It concatenates the tsv files from each sample and creates a single file
Author: Riddhika

'''

import os
import sys
import pandas as pd
from glob import glob
from os import walk

main_dir = sys.argv[1]
out_file = sys.argv[2]

try:
    sample = []
    file = []
    for root, dirs, files in os.walk(main_dir):
        for d in dirs:
            sample.append(d)
    df1 = pd.DataFrame(sample, columns=['SampleID'])

    for root, dirs, files in os.walk(main_dir):
        for filename in files:
            nm, ext = os.path.splitext(filename)
            if ext.lower().endswith(('.tsv')):
                fullpath = os.path.join(os.path.abspath(root), filename)
                file.append((fullpath))
    li = []
    for fnames in file:
        df2 = pd.read_csv(fnames, index_col=None, header=0, sep='\t')
        li.append(df2)
    frame = pd.concat(li,axis=0, ignore_index=True)

    results = pd.concat([df1, frame], axis=1, sort = False)
    del results['Unnamed: 0']
    results.to_string(index = False)
    print(results)
    results.to_excel(out_file)

except Exception as e:
    print("The error has occurred while running the HLA-Typing Report creation. An error is: {}".format(e))







