import argparse
import sys

# Create the parser
parser = argparse.ArgumentParser()
parser.add_argument("--test", type=bool, action=argparse.BooleanOptionalAction, help="If present, it will output the console messages but not save the edited bookmap config file. [True if present, False if not]")
parser.add_argument("--printlist", type=bool, action=argparse.BooleanOptionalAction, help="If present, it will output the symbols found in the config file. [True if present, False if not]")
parser.add_argument("--savelist", type=bool, action=argparse.BooleanOptionalAction, help="Save a list of chart configs to the local program directory. [True if present, False if not]")
parser.add_argument("--clearcharts", type=bool, action=argparse.BooleanOptionalAction, help="Clears the stored charts data. [True if present, False if not]")
parser.add_argument("--injecttocharts", type=bool, action=argparse.BooleanOptionalAction, help="Does not clear settings->charts, injects lastUsed into each one. Used for persisting the isInMainWindow and windowPosition settings for detached windows. [True if present, False if not, overrides the --clearcharts flag if present.]")
parser.add_argument("--extractsymbolsettings", type=str, nargs="?", const="use_default", metavar="MyExportName.cfg.json", help="Save the given symbolID to the local program directory, requires --symbolid . Follow with a given filename or it will use the SymbolID-name. [If present, please specify an export file name or use default.]")
parser.add_argument("--importtolastused", type=str, metavar="MyImportFile.cfg.json", help="Imports the specified file to the last used. Follow --importtolastused with a file name. File must be in this programs directory, not the bookmap directory. [If present, please specify a config filename]")
parser.add_argument("--symbolid", type=str, metavar="AMD@DXFEED12", help="The ID of the chart symbol you want to extract. e.g. 'AMD' -- The more specific, the more likely to grab the right one. Find the ID name by using the --savelist option to export the chart list to a .txt file.")

if len(sys.argv)==1:
    print('''
          NOTICE: No command parameters were given, program will exit with no actions. 
          Please see the help readme.md or information on the GitHub.
          
          @Author: Kyle Kimsey <kael29lv[at]gmail.com>
          @Version: 1.0.0
          @GitHub: https://github.com/kylek29/bookmap-tos-config/blob/main/README.md

          Command Usage:
          ''')
    parser.print_usage()
    sys.exit(0)
args = parser.parse_args()


