"""
Created on Mon Jun 13 12:23:52 2022

@author: Kyle Kimsey
@github: https://github.com/kylek29/bookmap-tos-config/blob/main/README.md
"""
__version__ = '1.0.0'
__author__ = 'Kyle Kimsey <kael29lv[at]gmail.com>'

import bookmaptosconfighelper.bm_config_parser as bm
import bookmaptosconfighelper.arg_parser as args
import bookmaptosconfighelper.settings_parser as settings
import os
import sys
import time
import json
import shutil
import pathlib 

# Helper parameters
BACKUP_DIRECTORY = settings.cwd.joinpath("backup_configs")

# Helper Functions [export to help functions?]KLTEMP
def strip_quotes(txt):
    return txt.replace("'","").replace('"','')


def backup_bmconfig_file():
    # Make a copy of the Bookmap config file in our program directory.
    ts = int(time.time())
    src_name = f"{ts}_{settings.bmconfig}.bkup"
    dst_folder = settings.cwd.joinpath("backup_configs")
    dst_file = dst_folder.joinpath(src_name)
    
    # Create the backup_configs directory if it does not exist.
    dst_folder.mkdir(exist_ok=True)
    shutil.copy(settings.bm_full_config_file, dst_file)     


def backup_delete_oldest(keep: int = 20):
    # Delete the oldest backup(s) after the N[keep]
    keep = int(keep)
    files = searching_all_files(BACKUP_DIRECTORY)
    files.sort(reverse=True)
    file_count_diff = len(files) - keep
    
    if len(files) > keep:
        print(f"-- .. purging oldest files, keeping latest {keep} files.")
        _files_to_del = files[-file_count_diff:]
        
        for file in _files_to_del:
            if file.suffix == ".bkup":
                print(f".. deleting old backup file {file.name}")
                file.unlink()
    return files


def searching_all_files(directory: pathlib.Path):   
    file_list = [] # A list for storing files existing in directories
    for f in directory.iterdir():
        if f.is_file():
           file_list.append(f)
        else:
           file_list.append(searching_all_files(directory/f))
    return file_list


def check_permissions(path: pathlib.Path):
    # Take in a path str and file 
    _ts = int(time.time())
    _tmpfile = path.joinpath(f"__tmp{_ts}.tmp")
    
    try:
        filehandle = open(_tmpfile, 'w')
        filehandle.close()
        os.remove(_tmpfile)
        return True
    except PermissionError:
        print(f"ERROR - Permission Error: Trouble writing temp file to {path}")
        return False 
    
    
if __name__ == '__main__':    
    # Check program directory for write access
    if not check_permissions(settings.cwd):
        raise PermissionError(f"Sorry, we do not have permission to write to the {settings.cwd} directory.")
    
    # Check Bookmap Settings directory for write access
    if not check_permissions(settings.bm_full_settings_dir):
        raise PermissionError(f"Sorry, we do not have permission to write to the {settings.bm_full_settings_dir} directory.")
    
    # Load Bookmap config file into program.
    try:
        file = open(settings.bm_full_config_file, 'r')
    except FileNotFoundError:
        print(f"-- ERROR -- FileNotFound: {settings.bm_full_config_file}, please verify your Bookmap install directory settings [config.ini -> bookmap_config_file].\n")
        print("-- Exiting program ...")
        sys.exit(0)
        
    bmcfg = json.load(file)
    bmeditor = bm.BookmapToSConfigEditor(bmcfg)
    
    # Argument Handling
    args = args.args
    #print(args) #KLTEMP
    
    # Save the Symbol List and exit program.
    if args.savelist:
        print("-- Requested to save list, saving to SymbolsList.txt in program directory. Exiting program.")
        bmeditor.save_symbols_list() #Uncomment
        sys.exit(0)
        
    # Print the Symbol List if specified.
    if args.printlist:
        print(f"-- Outputting symbol list, total symbols found: {bmeditor.print_symbols_count()} \n")
        bmeditor.print_symbols()
        sys.exit(0)
        
    # Get any Symbol ID passed in.
    if args.symbolid:
        # Strip quotes if given.
        args.symbolid = strip_quotes(args.symbolid)
        print(f"-- Symbol ID given: {args.symbolid}")
        
    # Extract given SymbolID to a config file.
    if args.extractsymbolsettings:
        if not args.symbolid:
            print("ERROR -- No [SymbolID] was given, please specify a SymbolID as --symbolid 'MYSYMBOL' and try again.")
            sys.exit(0)
        else:
            if args.extractsymbolsettings == 'use_default':
                export_filename = bmeditor.extract_symbol_config(args.symbolid)
            else:
                export_filename = bmeditor.extract_symbol_config(args.symbolid, filename=args.extractsymbolsettings)
            _cwd = settings.cwd.joinpath(export_filename)
            print(f"-- Extracting {args.symbolid} as {export_filename} to file: {_cwd}")
       
    # Import the settings to lastUsed.
    if args.importtolastused:
        import_file_to_use = strip_quotes(args.importtolastused)
        imported_file = open(import_file_to_use)
        bmeditor.overwrite_lastused(imported_file)
        print(f"-- .. replacing lastUsed with the given config {import_file_to_use}") 
        # Inject settings to charts?
        if args.injecttocharts:
            args.clearcharts = False
            imported_file = open(import_file_to_use)
            bmeditor.update_charts_with_config(imported_file)
            print("-- .. injecting the provided config file into all prior charts.")
        
    if args.clearcharts:
        print("-- .. clearing old charts data.")
        bmeditor.clear_charts()
        
    if args.test:
        print("NOTICE: Ran with the --test switch, the master Bookmap config file was not saved to disk.")
        sys.exit(0)
    else: 
        # Backup settings file, purge oldest N versions
        backup_bmconfig_file()
        backup_delete_oldest(keep=settings.backups)
        # Save the config file out
        bmeditor.save_config(filename=settings.bm_full_config_file)
        print(f"-- Updating Bookmap config in folder: {settings.bm_full_config_file}")
        sys.exit(0)
        
