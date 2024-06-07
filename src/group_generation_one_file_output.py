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
from pathlib import Path
from random import shuffle
from helper.file_operation import get_string_list_from_file, get_file_name_without_ending,\
    write_list_to_file


PROGRAM_NAME = 'Group Shuffle - Generate one file'
PROGRAM_VERSION = '0.0.1'
PROGRAM_DESCRIPTION = 'shuffle groups to one file'


def setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('original_file_folder', type=str)
    parser.add_argument('output_file', type=str)
    parser.add_argument('-n', '--number_of_groups', type=int, default=12, help='number of groups')
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages and show browser')
    return parser.parse_args()


def get_specific_files_in_dir(folder, filter_pattern='*'):
    dir_path = Path(folder)
    return [f for f in dir_path.glob(filter_pattern)]


def correct_form(user_entry, group_name):
    entry = user_entry.split(';')
    result = [group_name, entry[1], entry[0], entry[2]]
    return ';'.join(result)


def get_shuffled_groups_from_file(file_path, number_of_groups):
    result = list()
    original_entries = get_string_list_from_file(file_path)
    shuffle(original_entries)
    group_size = len(original_entries)
    group_name = get_file_name_without_ending(file_path)
    sub_group_size = int(len(original_entries) / number_of_groups)

    for group_id in range(number_of_groups):
        sub_group_name = '{}_msg-{}'.format(group_name, group_id+1)
        for user_index in range(sub_group_size):
            current_user = original_entries.pop()
            result.append(correct_form(current_user, sub_group_name))
    print('group: {}; members: {}; sub-group-size: {}; members ignored: {}'.format(
        group_name,
        group_size,
        sub_group_size,
        len(original_entries)))
    return result



if __name__ == '__main__':

    args = setup_argparser()

    original_files = get_specific_files_in_dir(args.original_file_folder, filter_pattern='*.csv')

    all_entries = list()

    for current_file in original_files:
        all_entries.extend(get_shuffled_groups_from_file(current_file, args.number_of_groups))

    write_list_to_file(all_entries, args.output_file)

    sys.exit(0)
