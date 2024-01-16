#! /usr/bin/env python3
'''
    Group Shuffle
    Copyright (C) 2024 Universitaetsklinikum Bonn AoeR

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse
import sys
import os
from random import shuffle

from helper.file_operation import get_string_list_from_file, write_list_to_file
from delete_entries import remove_duplicates_in_list

PROGRAM_NAME = 'Group Shuffle - Generate Random Groups'
PROGRAM_DESCRIPTION = 'PLACEHOLDER'


def setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument("-f", "--input_file", required=True, help="the path to the textfile with the data")
    parser.add_argument("-p", "--output_path", required=True, help="the path to the folder where the generated files will be saved")
    parser.add_argument("-n", "--number_of_groups", type=int, default=12, help="the number of textfiles that will be generated")
    return parser.parse_args()

def generate_output_path(output_path):
    os.makedirs(output_path, exist_ok=True)

def generate_output_files(number_of_groups, group_size, output_list, output_path):   
    for i in range(0, number_of_groups):
        starting_index = i*group_size
        current_group = output_list[starting_index:starting_index+group_size]
        output_file = output_path + "group" + str(i+1) + ".txt"
        write_list_to_file(current_group, output_file) 


if __name__ == '__main__':

    args = setup_argparser()

    input_list = get_string_list_from_file(args.input_file)
    output_list = remove_duplicates_in_list(input_list)
    shuffle(output_list)
    
    total_number_of_entries = len(output_list)
    group_size = (int)(total_number_of_entries / args.number_of_groups)

    generate_output_path(args.output_path)
    generate_output_files(args.number_of_groups, group_size, output_list, args.output_path)
    
    print(str(args.number_of_groups) + " random groups of " + str(group_size) + " colleagues each have been generated.")

    sys.exit(0)
