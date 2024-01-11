#! /usr/bin/env python3


import argparse
import os
from helper import file_operation
from random import shuffle


# get file, path and number=12 with argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--input_file", required=True, help="the path to the textfile with the data")
parser.add_argument("-p", "--output_path", required=True, help="the path to the folder where the generated files will be saved")
parser.add_argument("-n", "--number_of_groups", type=int, default=12, help="the number of textfiles that will be generated")
args = vars(parser.parse_args())

data_list = file_operation.get_string_list_from_file(args["input_file"])
shuffle(data_list)

total_number_of_entries = len(data_list)
group_size = (int)(total_number_of_entries / args["number_of_groups"])

os.makedirs(args["output_path"], exist_ok=True)

# save entries into new textfiles
for i in range(0, args["number_of_groups"]):
    starting_index = i*group_size
    current_group = data_list[starting_index:starting_index+group_size]
    output_file = args["output_path"] + "group" + str(i+1) + ".txt"
    file_operation.write_list_to_file(current_group, output_file)

print(str(args["number_of_groups"]) + " random groups of " + str(group_size) + " colleagues each have been generated.")

