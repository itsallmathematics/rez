import json
from enum import Enum

class ImportType(Enum):
    JSON = 1
    ODF = 2
    DOCX = 3
    PDF = 4

class Importer:
    def __init__(self, prof, profType):
        self._profType = profType
        self._prof = prof

    def profileImport(self): #TODO: Add filename in init and also support other ImportTypes
        with open("../tests/profile.json", "r") as f:
            self._prof.__dict__ = json.load(f)

