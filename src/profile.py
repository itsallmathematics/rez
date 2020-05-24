import json
from importer import Importer, ImportType
from exporter import Exporter, ExportType
import importer
class Profile():
    def __init__(self):
        self._firstName = None
        self._lastName = None
        self._middleName = None
        self._mobile = None
        self._education = None
        self._skills = None
        self._email = None

    def __str__(self):
        output = (
            f"First Name: {self._firstName}\n"
            f"Last Name: {self._lastName}\n"
            f"Middle Name: {self._middleName}\n"
            f"Education: {self._education}\n"
            f"Mobile: {self._mobile}\n"
            f"Email: {self._email}\n"
        )
        return output

    def promptData(self):
        print('Enter your information when prompted. All provided info appears on resume')
        self._firstName = input("Enter your first name: ")
        self._lastName = input("Last Name: ")
        maybeMiddleName = input("Middle name or n for none: ")
        if maybeMiddleName.lower() != "n" :
            self._middleName = maybeMiddleName
        self._education = input("Education: ")
        maybeMobile = input("Mmobile number or n for no number: ")
        if maybeMobile.lower() != 'n':
            self._mobile = maybeMobile
        self._email = input("Email: ")

    def load(self):
        imp = Importer(self, ImportType.JSON)
        imp.profileImport()


    @property
    def education(self):
        return self._education

    @education.setter
    def education(self, ed):
        self._education = ed


class Education():
    def __init__(self, school, years, degree):
        self._school_name = school
        self._years_attended = years
        self._degree = degree

if __name__ == '__main__':

    prof = Profile()
    imp = Importer(prof, ImportType.JSON)
    imp.profileImport()
    print(prof)
