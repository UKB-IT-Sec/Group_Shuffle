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

from helper.file_operation import get_string_list_from_file, write_list_to_file

PROGRAM_NAME = 'Group Shuffle - Delete Entries'
PROGRAM_VERSION = '0.2'
PROGRAM_DESCRIPTION = 'Delete double entries and filter unwanted entries'


def setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('original_file')
    parser.add_argument('output_file')
    parser.add_argument('-B', '--blacklist_file', default=None, help='blacklist with unwanted entries')
    parser.add_argument('-w', '--whitelist_string_filter', default=None, help='delete all entries not containing this string')
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages and show browser')
    return parser.parse_args()


def remove_duplicates_in_list(input_list):
    return list(set(input_list))


def apply_blacklist(original_list, blacklist):
    cleaned_list = list()
    for entry in original_list:
        if entry not in blacklist:
            cleaned_list.append(entry)
    return cleaned_list
    

def apply_whitelist_string_filter(original_list, filter_string):
    cleaned_list = list()
    for item in original_list:
        if filter_string in item:
            cleaned_list.append(item)
    return cleaned_list


if __name__ == '__main__':
    
    args = setup_argparser()
    
    original_list = get_string_list_from_file(args.original_file)
    print('Items in original list: {}'.format(len(original_list)))

    tmp_list = remove_duplicates_in_list(original_list)
    
    if args.blacklist_file:
        blacklist = get_string_list_from_file(args.blacklist_file)
        tmp_list = apply_blacklist(tmp_list, blacklist)
        
    if args.whitelist_string_filter:
        tmp_list = apply_whitelist_string_filter(tmp_list, args.whitelist_string_filter)

    write_list_to_file(tmp_list, args.output_file)
    print('Items in cleaned list: {}'.format(len(tmp_list)))
    
    sys.exit(0)