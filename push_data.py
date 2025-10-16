import os 
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetSecurityException
from networksecurity.logging.logger import logging
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
ca=certifi.where()


class NetDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetSecurityException(e,sys)
        
    def insert_mongodb(self, records, database,collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetSecurityException(e,sys)
        


if __name__ == "__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="RevanthDB"
    Collection="NetworkData"
    networkobj=NetDataExtract()
    records=networkobj.cv_to_json_convertor(FILE_PATH)
    print(records)
    num_records=networkobj.insert_mongodb(records,DATABASE,Collection)
    print(num_records)