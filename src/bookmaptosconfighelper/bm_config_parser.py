from copy import deepcopy
import json
import sys

class BookmapToSConfigEditor():
    """
    Class object for the Bookmap Think-or-Swim Config file.
    """
    
    def __init__(self, file: dict):
        self._config = file
        self._config_old = deepcopy(file)
        self.symbol_list = dict()
        self.parse_symbols()
    
    def parse_symbols(self):
        # Extracts the symbol configs in the file and puts into symbol_list. 
        try:
            for idx, cfg in enumerate(self._config['settings']['charts']):            
                self.symbol_list[cfg['symbol'].upper()] = self.SymbolConfig(
                    symbol_index = idx, symbol_config = cfg)
        except KeyError:
            print("NOTICE: No existing chart configs found.")

    def get_symbol_config(self, search_symbol:str, return_nameid:bool = False):
        # Returns the first match for the given string. Be exact for closer.
        search_symbol = search_symbol.upper()
        _sorted = sorted(self.symbol_list.items())       
        for sym, obj in _sorted:
            if sym[:len(search_symbol)] == search_symbol:
                if(return_nameid):
                    return sym
                else:
                    return obj
        print(("ERROR: No symbol matched the search string, check the list " \
               "of symbols with the print_symbols() method."))   
    
    def clear_charts(self):
        # Deletes all the existing symbol configs in the file.
        del self._config['settings']['charts']
    
    def print_symbols(self, print_columns:bool = True):
        # Prints a human-friendly list of the symbols.
        for sym in self.symbol_list.keys():
            cfg = self.symbol_list[sym]
            print(cfg.id, sym)
            if print_columns:
                for idx in cfg.columns:
                    print(f"> Column Title: {idx[0]} -> Type: {idx[1]}")           
                print("-----")
            
    def save_symbols_list(self, print_columns:bool = True):
        # Saves out the symbols list
        orig_stdout = sys.stdout
        with open("SymbolList.txt", "w") as file:
            sys.stdout = file
            self.print_symbols()
            sys.stdout = orig_stdout
            
    def print_symbols_count(self):
        # Prints the number of symbols found in settings --> charts.
        return len([1 for k in enumerate(self.symbol_list.keys())])
    
    def extract_symbol_config(self, name: str, filename: str = None):
        # Given a config symbol ID, it extracts the closest match to a cfg file.
        _data = self.get_symbol_config(search_symbol = name)
        if not filename:
            filename = f"{_data.title}_cfg.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(_data.config, f, ensure_ascii=False, indent=4)
            print(f"Found config: '{_data.title}' for given name '{name}', saved as" \
                  f"'{_data.title}_cfg.json' in program directory.")
        return filename

    def overwrite_lastused(self, config):
        """
        Overwrites the last-used in the config given a compatible config FILE \
            or an existing symbol name from the current config to lookup.
        """
        try:
            del self._config['settings']['lastUsed']
        except KeyError:
            print("-- .. lastUsed was already cleared, proceeding")
        if(type(config) == str):
            new_last_cfg = self.get_symbol_config(config)   
            self._config['settings']['lastUsed'] = new_last_cfg.config
        else:
            loaded_config = config.read()
            new_last_cfg = json.loads(loaded_config)
            self._config['settings']['lastUsed'] = new_last_cfg  

            
    def update_charts_with_config(self, config):
        """
        Given a compatible config FILE, loop through and replace the 
            settings of all existing configs but leave the window 
            configs (for detached windows).       
        """      
        if(type(config) == str):
            _cfg = deepcopy(self.get_symbol_config(config))
            new_cfg = _cfg.config
        else:
            loaded_config = config.read()
            new_cfg = json.loads(loaded_config)

        try:
            del new_cfg['symbol']
        except KeyError:
            pass
        
        try:
            del new_cfg['isInMainWindow']
        except KeyError:
            pass
        
        try:
            del new_cfg['windowPosition']
        except KeyError:
            pass        
        
        for i, cfg in enumerate(self._config['settings']['charts']):
            self._config['settings']['charts'][i] = self._config['settings']['charts'][i] | new_cfg
                      
        return True
            
            
    def save_config(self, filename = "bookmap_config_v7.json"):
        # Saves out the edits to the config to the default name unless defined.
        print(f"Saving config to {filename}") #KLDEBUG TEMP
        with open(filename, "w") as f:
            json.dump(self._config, f, indent=4) 
            #self.print_symbols()
            
    def _object_helper(self):
        # Debug class for quickly checking the object symbols.
        print(f"Original Config: {self._config_old['settings']['lastUsed']['symbol']}" \
              f"\n New Config: {self._config['settings']['lastUsed']['symbol']}")
    
    
    class SymbolConfig():
        """ Inner class that allows easy access to the attributes we need """
        
        def __init__(self, symbol_index:int, symbol_config: dict):
            self.id = symbol_index
            self.config = symbol_config
            self.title = symbol_config['symbol']
            self.columns = [(idc['title'], idc['type']) for idc in symbol_config['columns']]
