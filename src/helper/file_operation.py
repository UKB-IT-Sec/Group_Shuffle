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
import sys
import os


def get_string_list_from_file(file_path):
    try:
        with open(file_path) as source_file:
            lines = source_file.readlines()
    except Exception as e:
        sys.exit('Could not extract data from file: {}\nErrormessage: {} {}'.format(file_path, sys.exc_info()[0].__name__, e))
    return lines


def write_list_to_file(input_list, file_path):
    try:
        with open(file_path, mode='w') as output_file:
            output_file.writelines(input_list)
    except Exception as e:
        sys.exit('Could not write data to file: {}\n Errormessage: {} {}'.format(file_path, sys.exc_info()[0].__name__, e))


def get_file_name_without_ending(file_path):
    return file_path.stem


def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)
