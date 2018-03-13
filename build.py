#!/usr/bin/env python3
import os, os.path
import shutil
import subprocess

SROOT = 'src'
DROOT = 'dist'

def main():

    # setup
    if not os.path.exists(DROOT):
        os.mkdir(DROOT)
    if os.path.exists(os.path.join(SROOT, '__javascript__')):
        shutil.rmtree(os.path.join(SROOT, '__javascript__'))

    # transpile src/
    run('transcrypt -b -m --parent=.none src/main.py')
    shutil.copy(os.path.join(SROOT, '__javascript__', 'main.min.js'), os.path.join(DROOT, 'main.min.js'))
    shutil.copy(os.path.join(SROOT, '__javascript__', 'main.js'), os.path.join(DROOT, 'main.js'))




#########################
###  Helper functions

def run(cmd):
    print('\t' + cmd)
    subprocess.run(cmd, shell=True, check=True)


#########################
###  Start the program

if __name__ == '__main__':
    main()
