from google.appengine.ext import db
from google.appengine.api import users

print "hello"


class Employee(db.Model):
    name = db.StringProperty(required=True)
    role = db.StringProperty(required=True, choices=set(["executive", "manager", "producer"]))

    def __init__(self, name, role):
        self.name = name
        self.role = role
        print "New Employee with name", name

    # def __repr__(self):
        # return "Employee ", self.role, self.role
