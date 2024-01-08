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

PROGRAM_NAME = 'Group Shuffle - Delete Entries'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'Delete double entries'


def setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('original_file')
    parser.add_argument('output_file')
    parser.add_argument('blacklist_file')
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages and show browser')
    return parser.parse_args() 


def get_string_list_from_file(file_path):
    try:
        with open(file_path) as source_file:
            lines = source_file.readlines()
    except Exception as e:
        sys.exit('Could not extract data from file: {} {}'.format(sys.exc_info()[0].__name__, e))
    return lines

def write_list_to_file(input_list, file_path):
    try:
        with open(file_path, mode='w') as output_file:
            output_file.writelines(input_list)
    except Exception as e:
        sys.exit('Could not write data to file: {} {}'.format(sys.exc_info()[0].__name__, e))


def remove_duplicates_in_list(input_list):
    return list(set(input_list))


if __name__ == '__main__':
    
    args = setup_argparser()
    
    original_list = get_string_list_from_file(args.original_file)
    print('Items in original list: {}'.format(len(original_list)))

    original_list = remove_duplicates_in_list(original_list)
    
    blacklist = get_string_list_from_file(args.blacklist_file)
    
    cleaned_list = list()
    for entry in original_list:
        if entry not in blacklist:
            cleaned_list.append(entry)

    write_list_to_file(cleaned_list, args.output_file)
    print('Items in cleaned list: {}'.format(len(cleaned_list)))
    
    sys.exit(0)