

class Student(object):

    def __init__(self, first, last, language):

        self.first = first
        self.last = last
        self.labguage = language

    @property
    def fullname(self):
        return "{}-{}".format(self.first,self.last)

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)


