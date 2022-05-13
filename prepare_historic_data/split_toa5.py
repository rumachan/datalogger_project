#!/usr/bin/env python

# # split a large toa5 file into hourly blocks and save each file; for upload to geonet-archive

import sys

myfile = sys.argv[1]
bigfile = open(myfile, 'r')
lines = bigfile.readlines()

headerlines = lines[0:4]
instcode = headerlines[0].split(sep=',')[3].strip('"')

#remove 4 header lines from lines list
del lines[:4]

sitecode = lines[0].split(sep=',')[2].strip('"')

count = 0
for line in lines:
    line.strip() #newline character
    
    if count == 0:
        firstdate = line.split(sep=',')[0].split(sep=' ')[0].strip('"') + 'T'
        firsttime = line.split(sep=',')[0].split(sep=' ')[1].strip('"').replace(':', '_', 3) + 'Z'
        filename = sitecode+'_'+firstdate+firsttime+'_'+instcode+'.toa5.csv'
        smallfile = open(filename, 'w')
        
        for hl in headerlines:
            hl.strip().strip()
            smallfile.writelines(hl)
                    
    obsmin = line.split(sep=',')[0][15:17] #minute of observation time
    if obsmin == '50':
        count = 0
        smallfile.writelines(line)
        smallfile.close()
    else:
        count += 1
        smallfile.writelines(line)
smallfile.close()
