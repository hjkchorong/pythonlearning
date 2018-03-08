import datetime

class Person(object):
    def __init__(self,name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastname

    def __str__(self):
        """return self's name"""
        return self.name

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def setAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days