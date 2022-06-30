# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:23:52 2022

@author: Kyle Kimsey
@github: https://github.com/kylek29/bookmap-tos-config/blob/main/README.md
"""
import configparser
import pathlib 

cwd = pathlib.Path.cwd()
config = configparser.ConfigParser()
config.read('config.ini')

try:
    bmpath = pathlib.Path(config['settings']['bookmap_directory'])
except KeyError:
    bmpath = pathlib.Path('C:\\Program Files\\thinkorswim\\book_map')
    
try:
    bmconfig = pathlib.Path(config['settings']['bookmap_config_file'])
except KeyError:
    bmconfig = pathlib.Path('bookmap_config_v7.json')

try:
    backups = config['settings']['backups']
except KeyError:
    backups = "10"
    
bm_full_settings_dir = bmpath.joinpath('settings')
bm_full_config_file = bm_full_settings_dir.joinpath(bmconfig)


    

