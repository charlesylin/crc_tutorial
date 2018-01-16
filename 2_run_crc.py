#!/usr/bin/python


#crc tutorial scripts
#2_run_crc.py
#calls CRC3




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
    print('#==========================III. CALLING CRC3===========================')
    print('#======================================================================')
    print('\n\n')


    #running circuitry on the consensus system
    #creates a sbatch bash script
    crc_folder = '%scrc/' % (projectFolder)


    analysis_name = 'MM1S'
    enhancer_path = '%srose/MM1S_H3K27AC_ROSE/MM1S_H3K27AC_peaks_SuperEnhancers_ENHANCER_TO_GENE.txt' % (projectFolder)
    subpeak_path = '%smacsEnriched/MM1S_ATAC.bt2.srt.rmdup.macs14_peaks.bed' % (projectFolder)
    activity_path = '%stables/MM1S_EXPRESSION_ACTIVITY.txt' % (projectFolder)
    config_path = '%scrc_config.txt' % (whereAmI)
    #extra args

    args = '--config %s' % (config_path)

    print('ESTABLISHING INPUT FILES')
    for file_path in [enhancer_path,activity_path,subpeak_path,config_path]:
        if utils.checkOutput(file_path,0.1,0.1):
            print('FOUND %s' % (file_path))
        else:
            print('UNABLE TO FIND %s' % (file_path))
            sys.exit()            

    pipeline_dfci.call_crc(analysis_name,enhancer_path,subpeak_path,activity_path,genome,crc_folder,args,py27_path ='')    

#==========================================================================
#==================================THE END=================================
#==========================================================================

    
if __name__=="__main__":
    main()
