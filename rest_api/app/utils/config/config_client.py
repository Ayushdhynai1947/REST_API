import json

dev_conf = {
    "database":
        {"ur1": 'sqlite:///data.db'
         
            
        }
}



class ConfigClient:
    
    def __init__(self,env) -> None:
        if env == 'dev':
            self.config = dev_conf
        else:
            pass
        
    def get_value(self,section ,key):
        
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
        else:
            return None