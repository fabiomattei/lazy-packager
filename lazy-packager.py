#!/usr/bin/env python

'''
Created on the 9th of July 2016
@author: Fabio Mattei, Tommaso
'''

#======================
# imports
#======================
import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

#======================
# Main
#======================

if __name__ == '__main__':
    zipf = zipfile.ZipFile('projectname.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('projectfolder', zipf)
    zipf.close()
