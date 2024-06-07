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
import logging

from helper.file_operation import get_string_list_from_file, create_directory


PROGRAM_NAME = 'Group Shuffle - extract email lists'
PROGRAM_VERSION = '0.0.1'
PROGRAM_DESCRIPTION = 'store email adresses to one file per group'


def setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_directory', type=str)
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    return parser.parse_args()


if __name__ == '__main__':

    args = setup_argparser()

    users = get_string_list_from_file(args.input_file)

    create_directory(args.output_directory)

    user_database = dict()

    for user in users:
        user_info = user.split(';')
        if user_info[0] not in user_database:
            user_database[user_info[0]] = list()
        user_database[user_info[0]].append(user_info[-1].strip())

    for entry in user_database:
        output = '; '.join(user_database[entry])
        with open('{}/{}.txt'.format(args.output_directory, entry), 'w') as filepointer:
            filepointer.write(output)

    sys.exit(0)
