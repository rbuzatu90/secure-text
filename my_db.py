from google.appengine.ext import db

class Key(db.Model):
    key_id = db.StringProperty(required=True)
    public_part = db.StringProperty(required=True, multiline=True)

def reset_db():
    query = Key.all(keys_only=True)
    entries = query.fetch(1000)
    db.delete(entries)