# Bookmap Think-or-Swim Config Helper
A Python-based (self-contained EXE) program to help Think or Swim users extract and import their Bookmap configs, since currently (as of 6/13/2022) the ToS version of Bookmap lacks this functionality.

# Overview
In the standalone version of Bookmap, configurations for many settings and UI elements are stored under the SYMBOL data, thus each symbol can have it's own set of configs/layouts associated with it. This is easily managed by a right-click menu which lets you export, import, and transfer these configs to other symbols as you see fit. 

In the Think-or-Swim version of Bookmap, this functionality does not exist. Configs are still stored under Symbol data, but these configs are not manageable on a user level, meaning that if you setup a specific config for AMD, it will only be loaded on INTC (example symbols) if you have not loaded INTC before. There is no menu or user interface functions for exporting and importing these setups to each symbol.
