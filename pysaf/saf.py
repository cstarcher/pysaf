#!/usr/bin/env python3

"""Create an archive in Simple Archive Format for batch import into DSpace."""

import collections
import csv
import os
import os.path
import shutil
import tkinter
import tkinter.messagebox
import xml.etree.ElementTree as ET


class CreateArchive():
    """Class for creating archive."""

    def __init__(self, gs):
        """Class variables for CreateArchive class."""
        self.csv_path = gs.csv_path
        self.bit_path = gs.bit_path
        self.archive_path = gs.archive_path
        self.file_name_list = []
        self.bit_name_list = []
        self.duplicate_file_name_list = []
        self.duplicate_bit_name_list = []
        self.missing_file_list = []
        self.create_zip = gs.create_zip
        self.split_zip = gs.split_zip
        self.zip_size = int(gs.zip_size)
        self.zip_unit = gs.zip_unit
        self.create_license = gs.create_license
        self.license_file = gs.license_file
        self.license_bundle = gs.license_bundle
        self.license_text = gs.license_text
        self.restrict_access = gs.restrict_access
        self.group_name = gs.group_name
        self.saf_folder_list = []

    def create_file_name_list(self):
        """Create a list of file names from CSV file."""
        with open(self.csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            for row in reader:
                for header, data in zip(headers, row):
                    if header == 'filename':
                        for csv_file_name in data.split('||'):
                            self.file_name_list.append(csv_file_name)
        return self.file_name_list

    def create_bit_name_list(self):
        """Create a list of file names in Location of Files directory."""
        for dirpath, dirnames, filenames in os.walk(self.bit_path):
            for fname in filenames:
                self.bit_name_list.append(fname)
        return self.bit_name_list

    def duplicate_file_name(self):
        """Create a list of duplicate file names from CSV file and handle error."""
        self.create_file_name_list()
        self.duplicate_file_name_list = [k for k, v in collections.Counter(
            self.file_name_list).items() if v > 1]
        if len(self.duplicate_file_name_list) != 0:
            result = tkinter.messagebox.askquestion(
                        'Duplicate File Name Warning',
                        'There are duplicate file names in your CSV file.\n'
                        '\n'
                        'Would you like to proceed?\n'
                        )
            if result == 'yes':
                pass
            else:
                duplicate_file_name_string = 'Duplicate file names:\n'
                for fname in self.duplicate_file_name_list:
                    duplicate_file_name_string += '\n' + fname
                tkinter.messagebox.showwarning(
                    'Duplicate File Name Error',
                    '{}\n'.format(duplicate_file_name_string)
                    )
                raise IOError

    def duplicate_bit_name(self):
        """Create a list of duplicate file names in Location of Files directory and handle error."""
        self.create_bit_name_list()
        self.duplicate_bit_name_list = [k for k, v in collections.Counter(
            self.bit_name_list).items() if k in self.file_name_list and v > 1]
        if len(self.duplicate_bit_name_list) != 0:
            duplicate_bit_name_string = 'The following files have the same name:\n'
            for fname in self.duplicate_bit_name_list:
                duplicate_bit_name_string += '\n' + fname
            tkinter.messagebox.showwarning(
                'Duplicate File Error',
                '{}\n'.format(duplicate_bit_name_string)
                )
            raise IOError

    def missing_files(self):
        """Create a list of file names in CSV file that are missing in Location of Files directory."""
        self.missing_file_list = set.difference(
            set(self.file_name_list), set(self.bit_name_list))
        if len(self.missing_file_list) != 0:
            missing_file_string = 'The following files were not found:\n'
            for fname in self.missing_file_list:
                missing_file_string += '\n' + fname
            tkinter.messagebox.showwarning(
                'Missing Files Error',
                '{}\n'.format(missing_file_string)
                )
            raise IOError

    def new_dir(self, saf_dir, row_num):
        """Create new directory for each DSpace record."""
        os.makedirs(os.path.join(saf_dir, ('item_{}'.format(row_num))))

    def change_dir(self, saf_dir, row_num):
        """Change current working directory to newly created directory."""
        os.chdir(os.path.join(saf_dir, ('item_{}'.format(row_num))))

    def write_license(self, contents_file):
        """Write license information to contents file and write license text to license file."""
        contents_file.write('{}' '\t' 'BUNDLE:{}' '\n'.format(self.license_file,
                                                              self.license_bundle))
        with open('{}'.format(self.license_file), 'w', encoding='utf-8') as license:
            license.write('{}'.format(self.license_text))

    def write_contents_file(self, data):
        """Write file names to contents file and copy files to directory."""
        with open('contents', 'a', encoding='utf-8') as contents_file:
            for csv_file_name in data.split('||'):
                if self.restrict_access:
                    contents_file.write('{}' '\t' 'BUNDLE:ORIGINAL' '\t' 'permissions:-r {}' '\n'.format(
                        csv_file_name, self.group_name))
                else:
                    contents_file.write('{}' '\t' 'BUNDLE:ORIGINAL' '\n'.format(csv_file_name))
                for dirpath, dirnames, filenames in os.walk(self.bit_path):
                    for fname in filenames:
                        if csv_file_name == fname:
                            shutil.copy2(os.path.join(dirpath, fname), '.')
            if self.create_license:
                self.write_license(contents_file)

    def write_dc_metadata(self, header_split, data_split):
        """Write metadata to dublin core file."""
        for value in data_split:
            dc_value = ET.Element('dcvalue')
            dc_value.attrib['element'] = header_split[1]
            if len(header_split) == 3:
                dc_value.attrib['qualifier'] = header_split[2]
            dc_value.text = value
            if os.path.isfile('dublin_core.xml'):
                with open('dublin_core.xml', 'a', encoding='utf-8') as dc_file:
                    dc_file.write('  {}' '\n'.format(
                        str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))
            else:
                with open('dublin_core.xml', 'w', encoding='utf-8') as dc_file:
                    dc_file.write('<?xml version="1.0" encoding="UTF-8"?>' '\n')
                    dc_file.write('<dublin_core>' '\n')
                    dc_file.write('  {}' '\n'.format(
                        str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))

    def write_schema_metadata(self, schema_file, header_split, data_split, schema):
        """Write metadata to schema files other than dublin core."""
        for value in data_split:
            dc_value = ET.Element('dcvalue')
            dc_value.attrib['element'] = header_split[1]
            if len(header_split) == 3:
                dc_value.attrib['qualifier'] = header_split[2]
            dc_value.text = value
            if os.path.isfile(schema_file):
                with open(schema_file, 'a', encoding='utf-8') as dc_file:
                    dc_file.write('  {}' '\n'.format(
                        str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))
            else:
                with open(schema_file, 'a', encoding='utf-8') as dc_file:
                    dc_file.write('<?xml version="1.0" encoding="UTF-8"?>' '\n')
                    dc_file.write('<dublin_core schema="{}">' '\n'.format(schema))
                    dc_file.write('  {}' '\n'.format(
                        str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))

    def write_closing_tag(self):
        """Write closing tag to each xml file."""
        for file_name in os.listdir('.'):
            if file_name.endswith('xml'):
                with open(file_name, 'a', encoding='utf-8') as dc_file:
                    dc_file.write('</dublin_core>' '\n')

    def create_files(self, saf_dir, row_num, headers, row):
        """Write CSV metadata to appropriate files."""
        self.new_dir(saf_dir, row_num)
        self.change_dir(saf_dir, row_num)
        for header, data in zip(headers, row):
            header_split = header.split('.')
            schema = header_split[0]
            data_split = data.split('||')
            schema_file = 'metadata_{}.xml'.format(header_split[0])
            if data:
                if header_split[0] == 'filename':
                    self.write_contents_file(data)
                elif header_split[0] == 'dc':
                    self.write_dc_metadata(header_split, data_split)
                else:
                    self.write_schema_metadata(schema_file,
                                               header_split,
                                               data_split,
                                               schema)
        self.write_closing_tag()

    def open_csv(self):
        """Read CSV file if Split ZIP is not selected."""
        saf_folder_name = 'SimpleArchiveFormat'
        self.saf_folder_list.append(saf_folder_name)
        saf_dir = os.path.join(self.archive_path, saf_folder_name)
        with open(self.csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            row_num = 1
            for row in reader:
                self.create_files(saf_dir, row_num, headers, row)
                row_num += 1

    def open_csv_split(self):
        """Read CSV file if Split ZIP is selected."""
        with open(self.csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            saf_folder_number = 1
            row_num = 1
            total_size = 0
            if self.zip_unit == 'MB':
                zip_size = self.zip_size * 1000000
            else:
                zip_size = self.zip_size * 1000000000
            for row in reader:
                saf_folder_name = 'SimpleArchiveFormat{}'.format(saf_folder_number)
                saf_dir = os.path.join(self.archive_path, saf_folder_name)
                self.create_files(saf_dir, row_num, headers, row)
                files = [f for f in os.listdir('.') if os.path.isfile(f)]
                for f in files:
                    total_size += os.path.getsize(f)
                if total_size >= zip_size:
                    saf_folder_number += 1
                    saf_dir = os.path.join(self.archive_path, saf_folder_name)
                    cur_dir = os.getcwd()
                    cur_folder = os.path.split(cur_dir)[-1]
                    new_dir = os.path.join(saf_dir, cur_folder)
                    shutil.move(cur_dir, new_dir)
                    total_size = 0
                    files = [f for f in os.listdir('.') if os.path.isfile(f)]
                    for f in files:
                        total_size += os.path.getsize(f)
                if saf_folder_name not in self.saf_folder_list:
                    self.saf_folder_list.append(saf_folder_name)
                row_num += 1

    def zip_archive(self):
        """Create ZIP files for all archive directories."""
        dst_folder_list = os.listdir(self.archive_path)
        for folder in dst_folder_list:
            folder_path = os.path.join(self.archive_path, folder)
            if folder in self.saf_folder_list and os.path.isdir(folder_path):
                shutil.make_archive(folder_path, 'zip', folder_path)
