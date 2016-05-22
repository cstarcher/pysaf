#!/usr/bin/env python3

"""Handles message boxes for for reporting exceptions to user."""

import tkinter
import tkinter.messagebox


class TkError():
    """Class for handling message boxes."""

    def empty_csv_path_error():
        """Report error when Select CSV File is empty."""
        tkinter.messagebox.showwarning(
            'CSV Entry Error',
            'Please select a CSV File.'
            '\n'
            )

    def empty_bit_path_error():
        """Report error when Select Location of Files is empty."""
        tkinter.messagebox.showwarning(
            'File Entry Error',
            'Please select a Location of Files.'
            '\n'
            )

    def empty_archive_path_error():
        """Report error when Select Archive Destination is empty."""
        tkinter.messagebox.showwarning(
            'Destination Entry Error',
            'Please forgot to select an Archive Destination.'
            '\n'
            )

    def license_text_error():
        """Report error when Create License is selected but license text is empty."""
        tkinter.messagebox.showwarning(
            'License Entry Error',
            'Please enter License Text.'
            '\n'
            )

    def type_error():
        """Report error when Select CSV File file is not a CSV file."""
        tkinter.messagebox.showwarning(
            'CSV File Error',
            'This file is not a CSV file.\n'
            '\n'
            'Please select a different file or save this file as CSV.'
            '\n'
            )

    def unicode_decode_error():
        """Report error when CSV file is not encoded as UTF-8."""
        tkinter.messagebox.showwarning(
            'Unicode Error',
            'Unfortunately, this file is not encoded correctly.\n'
            '\n'
            'I know it may not be convenient, but I must ask you to save this file as UTF-8.\n'
            '\n'
            'If you\'re not sure how to do that, you can find instructions here:\n'
            '\n'
            'https://github.com/cstarcher/pysaf'
            '\n'
            )

    def file_exists_error():
        """Report error when Select Archive Destination directory exists."""
        tkinter.messagebox.showwarning(
            'Folder Exists Error',
            'This destination already contains an archive folder.\n'
            '\n'
            'Please select a different Archive Destination.'
            '\n'
            )

    def index_error():
        """Report error when metadata field names in CSV file are not formatted correctly."""
        tkinter.messagebox.showwarning(
            'Metadata Field Error',
            'There is an error with your metadata field names.\n'
            '\n'
            'Please check your metadata field names.'
            '\n'
            )

    def unexpected_error():
        """Report error for all errors not previously handled."""
        tkinter.messagebox.showwarning(
            'Unexpected Error',
            'An unexpected error has occured.\n'
            '\n'
            'An error log has been created in the Archive Destination folder.\n'
            '\n'
            'It would be very helpful if you would report this error.\n'
            '\n'
            'You may report the error here:\n'
            '\n'
            'https://github.com/cstarcher/pysaf/issues\n'
            '\n'
            'Thank you for your help! I will respond as soon as possible.'
            '\n'
            )
