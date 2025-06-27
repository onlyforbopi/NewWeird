





import sys
import os
import time

try:
    import argparse
except:
    print("Failed to load argparse. Terminating")
    sys.exit(2)

# Initiate Parser
# MODIFY: CENTRAL HELP TEXT
parser = argparse.ArgumentParser(
        prog="FileSplitter_Fast", 
        formatter_class=argparse.RawDescriptionHelpFormatter, 
        #description="calculate X to the power of Y",
        description='''\
#            FileSplitter_Fast v.2
#            --------------------------------
#            Author: p.doulgeridis
#            Description: Splits a text file into a number
#            of files that have size = lines_in provided.
#
#        ''',
        epilog="Additional info")


#######
# Initiate mutually exclusive group. 
# SET BY DEFAULT FOR VERBOSE/QUIET
# IF YOU NEED MORE EXCLUSIVE OPTIONS, ADD A DIFFERENT GROUP.
#
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="count", default=0)
group.add_argument("-q", "--quiet", action="store_true")        


######
# Positional Arguments (Necessary)
# POSSIBLE KINDS (actions, types)
#
parser.add_argument("file", type=str, help="Provide the file")
parser.add_argument("lines", type=int, help="Provide the target lines")
parser.add_argument("start", type=int, help="Provide the beginning of substring - notepad++ column")
parser.add_argument("end", type=int, help="Provide the end of the substring - notepad++ column")


###### 
# Parse arguments
args = parser.parse_args()


######
# Assign arguments
# NUM_OF_LINES=args.lines
# filename = args.file



###################################################################
# wrappers 

# 
def reporting(lines_in):
    print("Operation Finished. Read: " + str(lines_in) + " lines.")


# file exists
def fileexists(filepath):
  '''
  Function: filexists
  Description: Checks for existence of file
  Input: filepath (or raw string of it)
  Output: Boolean
  Usage: if filexists(file_in):...
  Notes: Depending on system may need to 
  conver to raw string with r'file_in.
  '''
  import os.path
  if os.path.exists(filepath):
    return True
  else:
    return False    
    
    
#

#

#

#


try:
    file_in = args.file
    input_line_limit = args.lines
    
    
group = ""
prev_group = ""
file_count = 0
dict_group = {}


with open(file_in, 'r') as f:

    fout = open(str(file_in)  + ".out" + ".0.txt", "w")
    line_status = 0
    file_count += 1
    counter = 0
    last_line = ''
    
    
    for i, lines in enumerate(f):
        
        print("#####")
        print("Line: " + str(i) + " with content: " + str(lines))
        
        last_line = lines
        
        # parse group
        group = lines[2:6]
        
        
        # check if group is different than previous
        if group != prev_group:
        
            print("new group: " + str(group))
            
            # check line status
            print("Checking line status: " + str(line_status) + " <-> " + str(input_line_limit))
            if line_status < input_line_limit:
                if prev_group in dict_group.keys():
                    print("Writing to output")
                    for j in dict_group[prev_group]:
                        line_status += 1
                        fout.write(j)
            
            if line_status >= input_line_limit:
                print("Checking line status: " + str(line_status) + " <-> " + str(input_line_limit))
                print("Starting new file")
                #file_count += 1
                fout.close()
                fout = open(str(file_in) + ".out" + ".%d.txt"%(file_count), "w")
                file_count += 1
                line_status = 0
            
            # initialize new group
            dict_group = {}
            dict_group[group] = []
            
            # add line to group 
            dict_group[group].append(lines)
        
        else: 
        
            # same group
            dict_group[group].append(lines)
            
        prev_group = group
        
    fout.write(lines)
    fout.close()