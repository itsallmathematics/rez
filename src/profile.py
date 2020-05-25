import json
from importer import Importer, ImportType
from exporter import Exporter, ExportType
import importer
from enum import Enum

class Skill():
    def __init__(self, name):
        self._name = name
        self._type = None #TODO: add keyword lookup to determine this

    def __str__(self):
        return self._name

class SkillType(Enum):
    Technical = 1
    Soft = 2
class Profile():
    def __init__(self):
        self._firstName = None
        self._lastName = None
        self._middleName = None
        self._mobile = None
        self._education = None
        self._skills = []
        self._email = None

    def __str__(self):
        output = (
            f"First Name: {self._firstName}\n"
            f"Last Name: {self._lastName}\n"
            f"Middle Name: {self._middleName}\n"
            f"Education: {self._education}\n"
            f"Mobile: {self._mobile}\n"
            f"Email: {self._email}\n"
            f"Skills:{[str(s) for s in self._skills]}"
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
        print("Next, we need to add some skills to your resume. These are short items that an employer may be interested in, such as 'verbal communication', 'PHP7', 'C++11', etc...")
        while True:
            potential_skill = input("Enter a skill or 'done' to finish: ")
            if(potential_skill.lower() == "done"):
                break
            self.addSkill(potential_skill)

    def addSkill(self, name):
        self._skills.append(Skill(name))


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
