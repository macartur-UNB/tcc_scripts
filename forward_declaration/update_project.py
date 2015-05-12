#!/usr/bin/python

import glob
import random
import os
import sys


def update(_dir):
    cur_dir = os.getcwd()
    if _dir != ".":
        os.chdir(_dir)
    

    arg = "*.h"
    includes = glob.glob(arg)

    factors = [.10,.25,.50,.75,.90]
    factor = random.choice(factors)
    n = int(len(includes)*factor)
    files = random.sample(includes,n)

    for f in files:
        command = "touch {}".format(f)
        os.system(command)


    if _dir != ".":
        os.chdir(cur_dir)

if __name__ == "__main__":
    random.seed(204812345)

    _dir = "."
    if len(sys.argv) > 1:
        _dir = sys.argv[1]

    for i in range(10):
        update(_dir)
        command = "time make 2> /dev/null"
        os.system(command)


