#!/usr/bin/env python

from functions import *

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is ok!")

print(time_to_automate(40*60, 10, 4*12*10))
