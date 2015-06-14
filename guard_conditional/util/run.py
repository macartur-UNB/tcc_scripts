#!/usr/bin/python
import os

size = 10
if __name__ == "__main__": 
  for i in range(size):
    command = "time make > /dev/null"                                        
    text = os.system(command) 
