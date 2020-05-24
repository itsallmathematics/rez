import json
from enum import Enum

class ExportType(Enum):
    JSON = 1
    ODF = 2
    DOCX = 3
    PDF = 4

class Exporter:
    def __init__(self, prof, profType):
        self._profType = profType
        self._prof = prof

    def profileExport(self):
        with open("profile.json", "w") as f:
            j = json.dumps(self._prof.__dict__)
            f.write(j) #TODO: Add error handling try/except

    def profileImport(self):
        with open("profile.json", "r") as f:
            self._prof.__dict__ = json.load(f)

