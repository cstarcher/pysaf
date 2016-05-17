# PySAF
PySAF is an application for creating [Simple Archive Format](https://wiki.duraspace.org/display/DSDOC5x/Importing+and+Exporting+Items+via+Simple+Archive+Format#ImportingandExportingItemsviaSimpleArchiveFormat-DSpaceSimpleArchiveFormat) packages for upload to [DSpace](http://dspace.org/) repositories.

### Installation

##### Windows

There is a binary (.exe) file for Windows.

##### OS X

There is a binary (.dmg) file for OS X.

##### Linux

You will need to install using git. If you receive an ImportError for Tkinter, you will need to install the python-tk package.

```
sudo apt-get install python3-tk
```

##### Source

If you are installing from source, it is recommended to run this software using Python 3.5 or higher. This application only uses modules in the Python default package.

### How To Use

##### Metadata

You must save your metadata file as a .csv file. It must be encoded as UTF-8.

##### ZIP

Batch uploading into DSpace through the web UI requires the archive to be zipped. This application offers an option to zip your archive packages. You have the option to split the archive into multiple zip files and to set a maximum size limit for each file. The web UI limit for zip file size is 2 GB.

##### License

This application offers the option to create a license file for each item. This option will create a .txt file in each item directory with the license text you enter in the text entry box. It will also add the license file name and bundle:LICENSE tag to the contents file.

##### Access Restrictions

DSpace allows for access restrictions on individual bitstreams based on group permissions. This application allows the user to designate the group-level permissions for each of the files in the collection.
