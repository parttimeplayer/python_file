from data import Record
import json
from typing import List

class FileReader:
    def __init__(self, path):
        self.path = path

    def filereader(self) -> List[Record]:
        pass



class TextReader(FileReader):
    def filereader(self) -> List[Record]:
        recordlist = []
        f = open(self.path, "r", encoding= "UTF-8")
        text = f.readlines()
        for data in text:
            data = data.strip()
            record = Record(data.split(",")[0], data.split(",")[1], int(data.split(",")[2]), data.split(",")[3])
            recordlist.append(record)
        f.close()
        return recordlist
    
class JsonReader(FileReader):
    def filereader(self) -> List[Record]:
        recordlist = []
        f = open(self.path, "r", encoding= "UTF-8")
        text = f.readlines()
        for data in text:
            data = data.strip()
            data = json.loads(data)
            record = Record(data["date"], data["order_id"], int(data["money"]), data["province"])
            recordlist.append(record)
        f.close()
        return recordlist
