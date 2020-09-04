#!/usr/bin/env python3

from functions import *

# check_system()

"""with open("/Users/Rafael/Desktop/text.txt") as file:
    for line in file:
        print(line.strip().upper())
"""

print(read_a_csv_file("/Users/Rafael/Desktop/", "my_csv.csv"))

"""
with open("/Users/Rafael/Desktop/my_csv.csv", "w") as file:
    pass
with open ("/Users/Rafael/Desktop/my_csv.csv", "a") as file:
    file.write("Rafael Santos, 29, Genesys Application Specialist" + "\n" + "Gislaine Santos, 30, Designer")
"""
