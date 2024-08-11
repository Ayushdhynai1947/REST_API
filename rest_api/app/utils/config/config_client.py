import json

dev_conf = {
    "Database":
        {"ur1": 'sqlite:///data.db',
         "ur2": 'sqlite:///raw_sql.db',
         "uri3 ":  "mysql://root:ayush@localhost/students",
         
        },    
}


prod_conf = {
    "Database": {
        "uri" : ""
    }
}



class ConfigClient:
    
    def __init__(self,env) -> None:
        if env == 'dev':
            self.config = dev_conf
        else:
            self.config = prod_conf
        
    def get_value(self,section ,key):
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
        else:
            return None