TESTING

# PySAF
PySAF is an application for creating [Simple Archive Format](https://wiki.duraspace.org/display/DSDOC5x/Importing+and+Exporting+Items+via+Simple+Archive+Format#ImportingandExportingItemsviaSimpleArchiveFormat-DSpaceSimpleArchiveFormat) packages for upload to [DSpace](http://dspace.org/) repositories.

### Installation

##### Windows

There is an installer ([pysaf_win64.exe](https://github.com/cstarcher/pysaf/releases/download/v1.0.0/pysaf_win64.exe)) available for Windows.

To install, open the pysaf_win64.exe file. If you receive an unknown publisher error, select yes to continue the installation.

To run, select PySAF under Programs in the Start Menu. Alternately, you can click the Desktop shortcut if you chose this option during installation.

##### OS X

There is an installer ([pysaf_osx.dmg](https://github.com/cstarcher/pysaf/releases/download/v1.0.0/pysaf_macos.dmg)) available for OS X.

To install, open the pysaf_osx.dmg file and copy the application to your Applications folder.

To run, click the application in your Applications folder.

##### Linux

There is no installer package for Linux. You will need to download the source code.

If you receive an ImportError for Tkinter, you will need to install the python-tk package.

```
sudo apt-get install python3-tk
```

##### Source

To execute the source code, you should install Python version 3.5 or higher. This application only uses modules in the Python Standard Library.

```
python3 main.py
```

### How To Use

##### Select CSV File

You must save your metadata file as a .csv file. It must be encoded as UTF-8.

##### Select Location Of Files

This is the location of your item bitstreams (files) to be uploaded.

##### Select Archive Destination

This is the location on your computer to save the output archive packages and .zip files.

##### Create ZIP File

Batch uploading into DSpace through the web UI requires the archive to be zipped. This application offers an option to zip your archive packages. You have the option to split the archive into multiple .zip files and to set a maximum size limit for each file. The web UI upload limit for .zip file size is 2 GB.

##### Create License

This application offers the option to create a license file for each item. This option will create a .txt file in each item directory with the license text you enter in the text entry box. It will also add the license file name and bundle:LICENSE tag to the contents file.

##### Restrict Read Access

DSpace allows for read access restrictions on individual bitstreams based on group permissions. This application allows the user to designate the group-level permissions for each of the files in the collection.
