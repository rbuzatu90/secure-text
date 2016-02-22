from google.appengine.ext import db
from google.appengine.api import users


class Employee(db.Model):
    name = db.StringProperty(required=True)
    role = db.StringProperty(required=True, choices=set(["executive", "manager", "producer"]))

    def __init__(self, name, role):
        self.name = name
        self.role = role
        print "New Employee with name", name

    # def __repr__(self):
        # return "Employee ", self.role, self.role

class Key(db.Model):
    key_id = db.StringProperty(required=True)
    public_part = db.StringProperty(required=True, multiline=True)

    # def __init__(self, key_id, public_part):
    #     self.key_id = key_id
    #     self.public_part = public_part
    #     print "New key of ID", str(key_id)
    #     db.put(self)

# query = Key.all(keys_only=True)
# entries = query.fetch(1000)
# db.delete(entries)