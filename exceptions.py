#!/usr/bin/env python3

"""Placeholder."""

import tkinter
import tkinter.messagebox


class TkError():
    """Placeholder."""

    def empty_csv_path_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'CSV Entry Error',
            'Please select a CSV File.'
            )

    def empty_bit_path_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'File Entry Error',
            'Please select a Location of Files.'
            )

    def empty_archive_path_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'Destination Entry Error',
            'Please select an Archive Destination.'
            )

    def license_text_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'License Entry Error',
            'Please enter License Text.'
            )

    def type_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'CSV File Error',
            'This file is not a CSV file. '
            'Please select a different file.'
            )

    def destination_path_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'Destination Error',
            'You must specify the Output Destination for the archive.'
            )

    def file_exists_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'Folder Exists Error',
            'This destination already contains an archive folder. '
            'Please select a different Archive Destination.'
            )

    def unicode_decode_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'Unicode Error',
            'This file is not encoded correctly. '
            'Please save this file as UTF-8.'
            )

    def index_error():
        """Placeholder."""
        tkinter.messagebox.showwarning(
            'Metadata Field Error',
            'There is an error with your metadata field names. '
            'Please check your metadata field names.'
            )

    def DuplicateNameError():
        """Placeholder."""
        pass

    def DuplicateFileError():
        """Placeholder."""
        pass

    def DublinCoreError():
        """Placeholder."""
        pass
