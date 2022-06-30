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

It works by opening the Bookmap..[??].json file and provides helper functions to extract, import, and clear symbol config data. General usage is based on command-line arguments. The program will create backup copies before it saves out an edited config file, these will be stored as {epochtimestamp}_bookmap_config_v7.json.bkup in the utilities directory under the *backup_configs* folder. Example filename: 1656613872_bookmap_config_v7.json.bkup

- Source code is located in /src folder
- EXE is located in /build folder

# Install
There is no install, the program is designed to run from whatever folder you place it in. By default, it's aimed at the "C:\Program Files\thinkorswim\book_map" directory (default install for Think-or-Swim), but that can be changed in the Config.ini file.

As a general tip, it might be best to place the EXE somewhere in your user directory (e.g. C:\Users\*Username*\Documents ) so that you have full permissions to the local folder.

# Config.ini Options
- backups : [int] - default: 20 --> The number of backups the program will keep of the configs. With "10", it'll delete the 10th oldest file when a new one is successfully created.
- bookmap_directory : [str] - default: "C:\Program Files\thinkorswim\book_map" --> Path to the bookmap program file located inside the Think or Swim software directory, not the path to the config file.
- bookmap_config_file : [str] - default: "bookmap_config_v7.json" --> The name of the config file, you likely won't need to change this until they release a version 8 of Bookmap.

# Permissions
Windows 10 users may need to Run as Administrator or give permissions to edit the config file under the Think-or-Swim directory, this depends solely on your OS config.  A general check to see if we can write to the directory is performed with an Error Message being provided if that check fails.

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
1. Download and unpack to a folder where you want to story the utility.
2. Configure the config.ini as you see fit (otherwise, use defaults).
3. Call the program with a command to see the available configs in the BM settings file, e.g. program.exe --savelist
4. Check the list and find the settings you want to export to be your base template, note the ID. e.g. "AMD@DXFEED#2"
5. Call the program with an export command, e.g. program.exe --extractsymbolsettings --symbolid "AMD@DXFEED#2"
6. Call the program with an import command and how you want to apply it (clear all stored chart configs, or overwrite existing chart configs). e.g. program.exe --importtolastused "AMD@DXFEED#1_cfg.json" --injecttocharts

# Functions Available
| Action                  | Command Flag            | Type | Description / Usage                                                                                                                                                                                                    |
|-------------------------|-------------------------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Print SymbolList        | --printlist             | bool | Prints to console a list of symbols stored in the config file. Useful for trying to determine which to export.                                                                                                         |
| Save SymbolList         | --savelist              | bool | Same as above, but saves to a SymbolList.txt file in the utilities directory.                                                                                                                                          |
| Extract Symbol Settings | --extractsymbolsettings | str  | Given a --symbolid value, it will extract the closest match to that. If the settings you want to export are under ID: "AMD@DXFEED#3", you'd want to specify the the full name just in case there are other AMD charts. If a string is specified after the --extractsymbolsettings flag, it will save as that string. Otherwise the default filename pattern will be used. |
| Import to Last Used     | --importtolastused      | str  | Given an exported config filename, it will import that config to the lastUsed of the config. Combine with other flags.                                                                                                 |
| Inject to Charts        | --injecttocharts        | bool | If present, it will loop through all available charts and replace the configs for those charts with the given one excluding the window configs (this is useful for if you have detached windows).                      |
| Clear Charts            | --clearcharts           | bool | If present, it will clear the stored charts. This command is ignored if "--injecttocharts" is included in the flags.                                                                                                   |
| SymbolID                | --symbolid              | str  | Required for the --extractsymbolsettings flag to work.                                                                                                                                                                 |

\* bool type is True if flag is present, ignored otherwise.


|             | Command                                                                                                                                                                                                                                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example     | program.exe --savelist                                                                                                                                                                                                                                                                                                                                      |
| Description | Saves the stored configs to a SymbolList.txt file in the utilities directory.                                                                                                                                                                                                                                                                               |
|             |                                                                                                                                                                                                                                                                                                                                                             |
| Example     | program.exe --printlist                                                                                                                                                                                                                                                                                                                                     |
| Description | Prints the stored configs to the console.                                                                                                                                                                                                                                                                                                                   |
|             |                                                                                                                                                                                                                                                                                                                                                             |
| Example     | program.exe --extractsymbolsettings --symbolid "AMD"                                                                                                                                                                                                                                                                                                        |
| Description | Saves the first "AMD" config it can find to the utilities directory using the standard export pattern for the filename (e.g. "AMD@DXFEED#1_cfg.json").                                                                                                                                                                                                      |
|             |                                                                                                                                                                                                                                                                                                                                                             |
| Example     | `program.exe --extractsymbolsettings "MYFILENAME.JSON" --symbolid "AMD@DXFEED#3"     `                                                                                                                                                                                                                                                                        |
| Description | Saves the exact "AMD@DXFEED#3" config to the utilities directory as "MYFILENAME.JSON"                                                                                                                                                                                                                                                                       |
|             |                                                                                                                                                                                                                                                                                                                                                             |
| Example     | program.exe --importtolastused "MY_FILE.json"                                                                                                                                                                                                                                                                                                               |
| Description | Imports the settings stored in "MY_FILE.json" (under the utilities directory) into the lastUsed portion of the settings file.                                                                                                                                                                                                                               |
|             |                                                                                                                                                                                                                                                                                                                                                             |
| Example     | program.exe --importtolastused "MY_FILE.json" --injecttocharts                                                                                                                                                                                                                                                                                              |
| Description | Imports the settings stored in "MY_FILE.json" (under the utilities directory) into the lastUsed portion of the settings file AND also loops over all stored chart configs and replaces with these settings, excludes to replace the symbol-name, isInMainWindow, and windowPosition settings (for detached windows to remain where they were last present). |
|             |                                                                                                                                                                                                                                                                                                                                                             |
| Example     | program.exe --importtolastused "MY_FILE.json" --clearcharts                                                                                                                                                                                                                                                                                                 |
| Description | Imports the settings stored in "MY_FILE.json" (under the utilities directory) into the lastUsed portion of the settings file AND then clears out all stored chart configs. This will cause any symbol to inherit the lastUsed setting when pulled up in ToS.                                                                                                |
