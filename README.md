# Bookmap Think-or-Swim Config Helper
A Python-based (self-contained EXE) program to help Think or Swim users extract and import their Bookmap configs, since currently (as of 6/13/2022) the ToS version of Bookmap lacks this functionality.

Supported OS:
- Windows

Please note that periodic updates from TD Ameritrade for the Think-or-Swim software may break this utility (because of syntax change, config change, etc.). 

# Disclaimer
Author is not responsible for loss of data or corruption of config files. Use at your own risk.

# Overview
In the standalone version of Bookmap, configurations for many settings and UI elements are stored under the SYMBOL data, thus each symbol can have it's own set of configs/layouts associated with it. This is easily managed by a right-click menu which lets you export, import, and transfer these configs to other symbols as you see fit. 

In the Think-or-Swim version of Bookmap, this functionality does not exist. Configs are still stored under Symbol data, but these configs are not manageable on a user level, meaning that if you setup a specific config for AMD, it will only be loaded on INTC (example symbols) if you have not loaded INTC before. There is no menu or user interface functions for exporting and importing these setups to each symbol. 

# The Helper Program
This utility software is designed to allow you to manipulate these configs (with Think-or-Swim not running) in various ways to help ease the burden of trying to get the same config across all symbols you trade.

It works by opening the Bookmap..[??].json file and provides helper functions to extract, import, and clear symbol config data. General usage is based on command-line arguments. The program will create backup copies before it saves out an edited config file, these will be stored as Bookmap..[??].json-bak in the utilities directory. 

- Source code is located in /src folder
- EXE is located in /build folder

# Config.ini Options
- BackupCopies [...]
- BookmapPath [...] (Path to the program, not the config file!)

# Permissions
Windows 10 users may need to Run as Administrator or give permissions to edit the config file under the Think-or-Swim directory, this depends solely on your OS config. A general check to see if we can write to the directory is performed with an Error Message being provided if that check fails.

To set permissions on the folder so you don't need to Run as Administrator:
1. Navigate to your ToS Bookmap folder (by default, this is: C:\Program Files\thinkorswim\book_map ) and right-click the "settings" folder.
2. Select "Properties" from flyout menu
3. Select "Security" [tab]
4. Hit "Edit" button
5. Select "Users (*MYComputerName*\Users)" from the "Group or user names" list.
6. Under the "Permissions for Users" select "Allow" for "Full Control" option.
7. Hit "Apply"
8. Hit "OK"

# General Usage

# Functions Available
- Export List of Symbols (stored in the config file) --> Exports to the utilities directory
