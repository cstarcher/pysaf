#!/usr/bin/env python3

"""Main tkinter GUI file used by Windows OS."""

import exceptions
import logging
import os
import os.path
import saf
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class GuiTk():
    """Class for main tkinter GUI."""

    def __init__(self, root, gs):
        """Class variables for GuiTk class."""
        self.root = root
        self.root.title('PySAF')

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        self.dir_frame = ttk.Frame(self.main_frame)
        self.dir_frame.grid(row=1)

        self.zip_frame = ttk.Frame(self.main_frame)
        self.zip_frame.grid(row=2)

        self.license_frame = ttk.Frame(self.main_frame)
        self.license_frame.grid(row=3)

        self.access_frame = ttk.Frame(self.main_frame)
        self.access_frame.grid(row=4)

        self.create_frame = ttk.Frame(self.main_frame)
        self.create_frame.grid(row=5)

        self.progress_frame = ttk.Frame(self.main_frame)
        self.progress_frame.grid(row=6)

        self.csv_file_button = ttk.Button(self.dir_frame,
                                          width=25,
                                          text='Select CSV File',
                                          command=lambda: self.csv_file_open(gs))
        self.csv_file_button.grid(column=0, row=1, sticky='e')
        self.csv_file_var = tk.StringVar()
        self.csv_file_entry = ttk.Entry(self.dir_frame,
                                        width=60,
                                        textvariable=self.csv_file_var)
        self.csv_file_entry.grid(column=1, row=1, sticky='nsew')

        self.bit_dir_button = ttk.Button(self.dir_frame,
                                         width=25,
                                         text='Select Location of Files',
                                         command=lambda: self.bit_dir_open(gs))
        self.bit_dir_button.grid(column=0, row=2, sticky='e')
        self.bit_dir_var = tk.StringVar()
        self.bit_dir_entry = ttk.Entry(self.dir_frame,
                                       width=60,
                                       textvariable=self.bit_dir_var)
        self.bit_dir_entry.grid(column=1, row=2, sticky='nsew')

        self.archive_dir_button = ttk.Button(self.dir_frame,
                                             width=25,
                                             text='Select Archive Destination',
                                             command=lambda: self.archive_dir_open(gs))
        self.archive_dir_button.grid(column=0, row=3, sticky='e')
        self.archive_dir_var = tk.StringVar()
        self.archive_dir_entry = ttk.Entry(self.dir_frame,
                                           width=60,
                                           textvariable=self.archive_dir_var)
        self.archive_dir_entry.grid(column=1, row=3, sticky='nsew')

        self.zip_button_var = tk.IntVar()
        self.zip_button = ttk.Checkbutton(self.zip_frame,
                                          text='Create ZIP File',
                                          variable=self.zip_button_var,
                                          command=lambda: self.create_zip_button(gs))
        self.zip_button.grid(row=1, columnspan=3)

        self.license_button_var = tk.IntVar()
        self.license_button = ttk.Checkbutton(self.license_frame,
                                              text='Create License',
                                              variable=self.license_button_var,
                                              command=lambda: self.create_license_button(gs))
        self.license_button.grid(row=1, columnspan=2)

        self.access_button_var = tk.IntVar()
        self.access_button = ttk.Checkbutton(self.access_frame,
                                             text='Restrict Read Access',
                                             variable=self.access_button_var,
                                             command=lambda: self.restrict_access_button(gs))
        self.access_button.grid(row=1, columnspan=2)

        self.create_button = ttk.Button(self.create_frame,
                                        text='Create Archive',
                                        command=lambda: self.error_check(gs))
        self.create_button.grid(columnspan=2)

        for child in self.main_frame.winfo_children():
            child.grid_configure(padx=40, pady=15)

        for child in self.dir_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def csv_file_open(self, gs):
        """Open filedialog when Select CSV File button selected."""
        self.csv_file_path = filedialog.askopenfilename()
        gs.csv_path = self.csv_file_path
        self.csv_file_var.set(self.csv_file_path)

    def bit_dir_open(self, gs):
        """Open filedialog when Select Location of Files button selected."""
        self.bit_dir_path = filedialog.askdirectory()
        gs.bit_path = self.bit_dir_path
        self.bit_dir_var.set(self.bit_dir_path)

    def archive_dir_open(self, gs):
        """Open filedialog when Select Archive Destination button selected."""
        self.archive_dir_path = filedialog.askdirectory()
        gs.archive_path = self.archive_dir_path
        self.archive_dir_var.set(self.archive_dir_path)

    def create_zip_button(self, gs):
        """Expand frame to reveal options when Create ZIP File is selected."""
        if self.zip_button_var.get() == 1:
            self.split_button_var = tk.IntVar()
            self.split_button = ttk.Checkbutton(self.zip_frame,
                                                text='Split ZIP File',
                                                variable=self.split_button_var)
            self.split_button.grid(row=2, column=0, sticky='w')
            self.split_button.grid_configure(padx=2, pady=5)
            self.split_entry_var = tk.IntVar()
            self.split_entry = ttk.Entry(self.zip_frame,
                                         width=3,
                                         justify='right',
                                         textvariable=self.split_entry_var)
            self.split_entry.grid(row=2, column=1, sticky='e')
            self.split_entry.grid_configure(pady=5)
            self.split_entry_var.set('2')
            self.split_combo = ttk.Combobox(self.zip_frame,
                                            width=4,
                                            justify='left',
                                            values='MB GB')
            self.split_combo.current(1)
            self.split_combo.grid(row=2, column=2, sticky='w')
            self.split_combo.grid_configure(pady=5)
        else:
            self.split_button.destroy()
            self.split_entry.destroy()
            self.split_combo.destroy()

    def create_license_button(self, gs):
        """Expanded frame to reveal options when Create License is selected."""
        if self.license_button_var.get() == 1:
            self.license_file_label = ttk.Label(self.license_frame,
                                                width=20,
                                                anchor=tk.E,
                                                text='License File Name ')
            self.license_file_label.grid(row=2, column=0, sticky='e')
            self.license_file_var = tk.StringVar()
            self.license_file_entry = ttk.Entry(self.license_frame,
                                                width=20,
                                                textvariable=self.license_file_var)
            self.license_file_entry.grid(row=2, column=1, sticky='w')
            self.license_file_entry.grid_configure(pady=5)
            self.license_file_var.set('license.txt')

            self.license_bundle_label = ttk.Label(self.license_frame,
                                                  width=20,
                                                  anchor=tk.E,
                                                  text='Bundle Name ')
            self.license_bundle_label.grid(row=3, column=0, sticky='e')
            self.license_bundle_var = tk.StringVar()
            self.license_bundle_entry = ttk.Entry(self.license_frame,
                                                  width=20,
                                                  textvariable=self.license_bundle_var)
            self.license_bundle_entry.grid(row=3, column=1, sticky='w')
            self.license_bundle_entry.grid_configure(pady=5)
            self.license_bundle_var.set('LICENSE')

            self.license_text_label = ttk.Label(self.license_frame,
                                                text='Enter License Text Below:')
            self.license_text_label.grid(row=4, columnspan=2)
            self.license_text_label.grid_configure(pady=5)
            self.license_var = tk.StringVar()
            self.license_text = tk.Text(self.license_frame,
                                        height=5,
                                        width=65,
                                        highlightthickness=1,
                                        highlightcolor='gray',
                                        highlightbackground='gray')
            self.license_text.config(wrap='word')
            self.license_text.grid(row=5, columnspan=2)
            self.license_text.grid_configure(pady=5)
        else:
            self.license_file_label.destroy()
            self.license_file_entry.destroy()
            self.license_bundle_label.destroy()
            self.license_bundle_entry.destroy()
            self.license_text_label.destroy()
            self.license_text.destroy()

    def restrict_access_button(self, gs):
        """Expand frame to reveal options when Restrict Read Access is selected."""
        if self.access_button_var.get() == 1:
            self.group_name_label = ttk.Label(self.access_frame,
                                              width=20,
                                              anchor=tk.E,
                                              text='Group Name ')
            self.group_name_label.grid(row=2, column=0, sticky='e')
            self.group_name_label.grid_configure(pady=5)
            self.group_name_var = tk.StringVar()
            self.group_name_entry = ttk.Entry(self.access_frame,
                                              width=20,
                                              textvariable=self.group_name_var)
            self.group_name_entry.grid(row=2, column=1, sticky='w')
            self.group_name_entry.grid_configure(pady=5)
            self.group_name_var.set('member')
        else:
            self.group_name_label.destroy()
            self.group_name_entry.destroy()

    def get_vars(self, gs):
        """Get variables from tkinter widgets."""
        gs.csv_path = self.csv_file_var.get()
        gs.bit_path = self.bit_dir_var.get()
        gs.archive_path = self.archive_dir_var.get()
        if self.zip_button_var.get():
            gs.create_zip = self.zip_button_var.get()
            gs.split_zip = self.split_button_var.get()
            gs.zip_size = self.split_entry.get()
            gs.zip_unit = self.split_combo.get()
        else:
            gs.create_zip = self.zip_button_var.get()
        if self.license_button_var.get():
            gs.create_license = self.license_button_var.get()
            gs.license_file = self.license_file_entry.get()
            gs.license_bundle = self.license_bundle_entry.get()
            gs.license_text = self.license_text.get('1.0', 'end-1c')
        else:
            gs.create_license = self.license_button_var.get()
        if self.access_button_var.get():
            gs.restrict_access = self.access_button_var.get()
            gs.group_name = self.group_name_entry.get()
        else:
            gs.restrict_access = self.access_button_var.get()

    def update_archive_button(self):
        """Update Create Archive button to alert user to processing status."""
        if (self.create_button.config('text')[-1] == 'Create Archive'):
            self.create_button.config(text='Processing ... Please wait.')
            self.root.update_idletasks()
        elif (self.create_button.config('text')[-1] == 'Processing ... Please wait.'):
            self.create_button.config(text='Create Archive')
            self.root.update_idletasks()

    def create_archive(self, gs):
        """Handle method calls to CreateArchive class."""
        ca = saf.CreateArchive(gs)
        if ca.split_zip:
            ca.open_csv_split()
        else:
            ca.open_csv()
        if ca.create_zip:
            ca.zip_archive()

    def main(self, gs):
        """Change Create Archive button status before and after calls to CreateArchive class."""
        self.update_archive_button()
        self.create_archive(gs)
        self.update_archive_button()

    def error_check(self, gs):
        """Method for handling exceptions."""
        ca = saf.CreateArchive(gs)
        self.get_vars(gs)
        try:
            if not gs.csv_path:
                raise IOError
        except IOError:
            exceptions.TkError.empty_csv_path_error()
            self.create_button.config(text='Create Archive')
        else:
            try:
                if not gs.bit_path:
                    raise IOError
            except IOError:
                exceptions.TkError.empty_bit_path_error()
                self.create_button.config(text='Create Archive')
            else:
                try:
                    if not gs.archive_path:
                        raise IOError
                except IOError:
                    exceptions.TkError.empty_archive_path_error()
                    self.create_button.config(text='Create Archive')
                else:
                    try:
                        if gs.create_license:
                            if not gs.license_text:
                                raise IOError
                    except IOError:
                        exceptions.TkError.license_text_error()
                        self.create_button.config(text='Create Archive')
                    else:
                        try:
                            if not gs.csv_path.endswith('.csv'):
                                raise TypeError
                        except TypeError:
                            exceptions.TkError.type_error()
                            self.create_button.config(text='Create Archive')
                        else:
                            try:
                                ca.duplicate_file_name()
                            except IOError:
                                self.create_button.config(text='Create Archive')
                            except UnicodeDecodeError:
                                exceptions.TkError.unicode_decode_error()
                                self.create_button.config(text='Create Archive')
                            else:
                                try:
                                    ca.duplicate_bit_name()
                                except IOError:
                                    self.create_button.config(text='Create Archive')
                                else:
                                    try:
                                        ca.missing_files()
                                    except IOError:
                                        self.create_button.config(text='Create Archive')
                                    else:
                                        try:
                                            self.main(gs)
                                        except UnicodeDecodeError:
                                            exceptions.TkError.unicode_decode_error()
                                            self.create_button.config(text='Create Archive')
                                        except FileExistsError:
                                            exceptions.TkError.file_exists_error()
                                            self.create_button.config(text='Create Archive')
                                        except IndexError:
                                            exceptions.TkError.index_error()
                                            self.create_button.config(text='Create Archive')
                                        except Exception:
                                            logging.basicConfig(
                                                level=logging.DEBUG,
                                                filename=(os.path.join(
                                                    gs.archive_path,
                                                    'ErrorLog.txt'))
                                                    )
                                            logging.exception('Error')
                                            exceptions.TkError.unexpected_error()
                                            self.create_button.config(text='Create Archive')
