


import sys
import os
import time
import shutil


file_in = sys.argv[1]
file_ot = str(file_in) + ".bak"


def filebackup(file_in):
    '''
    Name: filebackup
    Description: Premade copy, appending .bak
    Input: <file_in> -> path to file
    Output: None
    Usage: filebackup(file_in)
    Notes: Windows path need \\ or r' ' 
    '''
    
    
    import os
    import shutil
    
    
    file_ot = str(file_in) + ".bak"
    try:
        shutil.copy(file_in, file_ot)
    except:
        print("prob")
        
print(filebackup(file_in))
print(help(filebackup))