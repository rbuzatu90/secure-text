from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4
from Crypto import Random
from my_db import Key, reset_db
import base64

def clear_db():
    reset_db()

def encrypt_text(text, key):
    query = Key.all()
    query.filter('key_id =', key)
    if query.fetch(1):
        public_key = query.fetch(1)[0].public_part # get the first item found in db and extract public_part attr
        my_key = RSA.importKey(public_key)
        encrypted_text = my_key.encrypt(str(text), 32)
        return base64.encodestring(encrypted_text[0])
    else:
        return "Key ID not found"

def encrypt_text_with_key(text, password):
    encryptor = ARC4.new(password)
    msg = encryptor.encrypt(text)
    return base64.encodestring(msg)

def decrypt_text_with_key(text, password):
    decryptor = ARC4.new(password)
    msg = decryptor.decrypt(base64.decodestring(text))
    return msg



def decrypt_text(text, key): # not ready yet
    query = Key.all()
    query.filter('key_id =', key)
    if query.fetch(1):
        public_key = query.fetch(1)[0].public_part # get the first item found in db and extract public_part attr
        my_key = RSA.importKey(public_key)
        print my_key

def generate_key(key_id, bits):
    query = Key.all()
    query.filter('key_id =', key_id)
    if query.fetch(1):
        print "Key already exists"
        return "Return: Key ID already exists"
    random_generator = Random.new().read
    print "Creating New Key with ID", key_id
    try:
        key = RSA.generate(int(bits), random_generator)
    except:
        return "Failed creating RSA Key"
    priv_part = key.exportKey()
    public_part_temp = key.publickey()
    public_part = public_part_temp.exportKey()
    my_key = Key(key_id=key_id, public_part=public_part)
    my_key.put()
    return public_part, priv_part

def load_public_key(key_id, key):
    query = Key.all()
    query.filter('key_id =', key_id)
    if query.fetch(1):
        print "Key already exists"
        return "Return: Key ID already exists"
    my_key = Key(key_id=key_id, public_part=key)
    my_key.put()
    return "Key Loaded"
