#!/usr/bin/env python3

"""Property decorators for getter and setter methods."""


class GetSet():
    """Class variables for GetSet class."""

    def __init__(self):
        """Placeholder."""
        self.csv_path = None
        self.bit_path = None
        self.archive_path = None
        self.create_zip = None
        self.split_zip = None
        self.zip_size = 0
        self.zip_unit = None
        self.create_license = None
        self.license_file = None
        self.license_bundle = None
        self.license_text = None
        self.restrict_access = None
        self.group_name = None

    @property
    def get_csv_path(self):
        """Property decorator for getting Select CSV File path."""
        return self.csv_path

    @get_csv_path.setter
    def set_csv_path(self, csv_path):
        """Setter for Select CSV File path."""
        self.csv_path = csv_path

    @property
    def get_bit_path(self):
        """Property decorator for getting Select Location of Files path."""
        return self.bit_path

    @get_bit_path.setter
    def set_bit_path(self, bit_path):
        """Setter for Select Location of Files path."""
        self.bit_path = bit_path

    @property
    def get_archive_path(self):
        """Property decorator for getting Select Archive Destination path."""
        return self.archive_path

    @get_archive_path.setter
    def set_archive_path(self, archive_path):
        """Setter for Select Archive Destination path."""
        self.archive_path = archive_path

    @property
    def get_create_zip(self):
        """Property decorator for getting Create ZIP File variable."""
        return self.create_zip

    @get_create_zip.setter
    def set_create_zip(self, create_zip):
        """Setter for Create ZIP File variable."""
        self.create_zip = create_zip

    @property
    def get_split_zip(self):
        """Property decorator for getting Split ZIP variable."""
        return self.split_zip

    @get_split_zip.setter
    def set_split_zip(self, split_zip):
        """Setter for Split ZIP variable."""
        self.split_zip = split_zip

    @property
    def get_zip_size(self):
        """Property decorator for getting ZIP size variable."""
        return self.zip_size

    @get_zip_size.setter
    def set_zip_size(self, zip_size):
        """Setter for ZIP size variable."""
        self.zip_size = zip_size

    @property
    def get_zip_unit(self):
        """Property decorator for getting ZIP unit variable."""
        return self.zip_unit

    @get_zip_unit.setter
    def set_zip_unit(self, zip_unit):
        """Setter for setting ZIP unit size."""
        self.zip_size = zip_unit

    @property
    def get_create_license(self):
        """Property decorator for getting Create License variable."""
        return self.create_license

    @get_create_license.setter
    def set_create_license(self, create_license):
        """Setter for Create License variable."""
        self.create_license = create_license

    @property
    def get_license_file(self):
        """Property decorator for getting License File Name."""
        return self.license_file

    @get_license_file.setter
    def set_license_file(self, license_file):
        """Setter for License File Name."""
        self.license_file = license_file

    @property
    def get_license_bundle(self):
        """Property decorator for getting License Bundle Name."""
        return self.license_bundle

    @get_license_bundle.setter
    def set_license_bundle(self, license_bundle):
        """Setter for License Bundle Name."""
        self.license_bundle = license_bundle

    @property
    def get_license_text(self):
        """Property decorator for getting Licenst text."""
        return self.license_text

    @get_license_text.setter
    def set_license_text(self, license_text):
        """Setter for License text."""
        self.license_text = license_text

    @property
    def get_restrict_access(self):
        """Property decorator for getting Restrict Read Access variable."""
        return self.restrict_access

    @get_restrict_access.setter
    def set_restrict_access(self, restrict_access):
        """Setter for Restrict Read Access variable."""
        self.restrict_access = restrict_access

    @property
    def get_group_name(self):
        """Property decorator for getting Group Name."""
        return self.group_name

    @get_group_name.setter
    def set_group_name(self, group_name):
        """Setter for Group Name."""
        self.group_name = group_name
