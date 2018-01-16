#!/usr/bin/python


#crc tutorial scripts
#0_summarize_data.py
#identifies datasets and dependencies necessary for tutorial




#==========================================================================
#=============================DEPENDENCIES=================================
#==========================================================================


import sys, os, string
# Get the script's full local path
whereAmI = os.path.dirname(os.path.realpath(__file__)) +'/'
print(whereAmI)

pipeline_dir = '/'.join(whereAmI.split('/')[0:-2]) + '/pipeline/'
print(pipeline_dir)


sys.path.append(whereAmI)
sys.path.append(pipeline_dir)

import pipeline_dfci
import utils
import string
import numpy
import os
import re
from collections import defaultdict
import subprocess
#==========================================================================
#============================PARAMETERS====================================
#==========================================================================



projectName = 'crc_tutorial'
genome ='hg19'
annotFile = '%s/annotation/%s_refseq.ucsc' % (pipeline_dir,genome)

#project folders
projectFolder = '/'.join(whereAmI.split('/')[0:-2]) + '/'
projectFolder = utils.formatFolder(projectFolder,True)


#mask Files



#==========================================================================
#============================LIST OF DATAFILES=============================
#==========================================================================

#this project will utilize multiple datatables
#data tables are organized largely by type/system
#some data tables overlap for ease of analysis

#ChIP-seq
chip_data_file = '%sdata_tables/MM1S_CHIP_TABLE.txt' % (projectFolder)

#ATAC-seq
atac_data_file = '%sdata_tables/MM1S_ATAC_TABLE.txt' % (projectFolder)

#==========================================================================
#===========================MAIN METHOD====================================
#==========================================================================


def main():


    print('main analysis for project %s' % (projectName))

    print('changing directory to project folder')
    os.chdir(projectFolder)

    print('\n\n')
    print('#======================================================================')
    print('#==================I. LOADING DATA ANNOTATION TABLES===================')
    print('#======================================================================')
    print('\n\n')

    #This section sanity checks each data table and makes sure both bam and .bai files are accessible

    #for chip data file
    pipeline_dfci.summary(chip_data_file)


    #for chip data file
    pipeline_dfci.summary(atac_data_file)

    print('\n\n')
    print('#======================================================================')
    print('#=====================II. CONFIGURING GENOME BUILD=====================')
    print('#======================================================================')
    print('\n\n')

    
    genome_directory = '%sgenomes/Homo_sapiens/UCSC/hg19/Sequence/Chromosomes/' % (projectFolder)
    mask_file =  '%sgenomes/Homo_sapiens/UCSC/hg19/Annotation/Masks/hg19_encode_blacklist.bed' % (projectFolder)
    
    config_table = [['BUILD:FIELD:PATH'],
                    ['%s:%s:%s' % (genome,'genome_directory',genome_directory)],
                    ['%s:%s:%s' % (genome,'mask_file',mask_file)],
                    ]
    config_path = '%scrc_config.txt' %(whereAmI)
    
    utils.unParseTable(config_table,config_path,'\t')
    print('writing genome configuration to %s' % (config_path))
#==========================================================================
#==================================THE END=================================
#==========================================================================

    
if __name__=="__main__":
    main()
