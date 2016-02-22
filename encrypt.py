from Crypto.PublicKey import RSA
from Crypto import Random
from my_db import Key

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

def encrypt_text(text, key):
    query = Key.all()
    query.filter('key_id =', key)
    if query.fetch(1):
        public_key = query.fetch(1)[0].public_part # get the first item found in db and extract public_part attr
        my_key = RSA.importKey(public_key)
        encrypted_text = my_key.encrypt(str(text), 32)
        return encrypted_text
    else:
        print "Key ID not found"
    # my_key = RSA.importKey(key)
    # lol = my_key.encrypt(text,key)

