# PySAF
PySAF is an application for creating [Simple Archive Format](https://wiki.duraspace.org/display/DSDOC5x/Importing+and+Exporting+Items+via+Simple+Archive+Format#ImportingandExportingItemsviaSimpleArchiveFormat-DSpaceSimpleArchiveFormat) packages for upload to [DSpace](http://dspace.org/) repositories.

### Installation

##### Windows

There is a 32-bit binary ([pysaf_win32.exe](https://texastechuniversity-my.sharepoint.com/personal/christopher_starcher_ttu_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=X4NmVO1P3sr904I8r0t4KGr4gYdPydyxmAhf1mkMM5o%3d&docid=008444389445241b69e32d3a2fbfc37bc)) and a 64-bit binary ([pysaf_win64.exe](https://texastechuniversity-my.sharepoint.com/personal/christopher_starcher_ttu_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=8YTPBhFVvqva%2bDVlJ3mFic6g11L3DNsHpkEGh%2bphf68%3d&docid=04a07ab040e8f44b88a5a16ce4d9dd280)) for Windows.

To install, open the pysaf_win32.exe or pysaf_win64.exe file. If you receive an unknown publisher error, select yes to continue the installation.

To run, select PySAF under Programs in the Start Menu. Alternately, you can click the Desktop shortcut if you chose this option during installation.

##### OS X

There is a binary ([pysaf_osx.dmg](https://texastechuniversity-my.sharepoint.com/personal/christopher_starcher_ttu_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=xtCahOezLbJP0JZxz29EsjrqzPsAXCpYsIkzPJfSnsM%3d&docid=0d8680d6eef3d4f519b3e1081b7fd7cd2)) available for OS X.

To install, open the pysaf_osx.dmg file and copy the application to your Applications folder.

To run, click the application in your Applications folder.

##### Linux

There is no binary package for Linux. You will need to download the source code.

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
