""" Author: Dumebi Umezinne
Purpose: To understand the MVC model/pattern.
"""

class Database:
    def __init__(self, path):
        """ 
        Constructor to create database of accounts/clients
         """
        with open(path, "r") as handle:
            #import json
            #self.data = json.load(handle)

            #import yaml
            #self.data = yaml.safe_load(handle)

            import xmltodict
            self.data = xmltodict.parse(handle.read())["root"]
            print(self.data)
    
    def balance(self, acct_id):
        """ 
        Calculates account balance for clients.
        """
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None
