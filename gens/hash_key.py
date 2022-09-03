import hashlib
import uuid

def key(salt, how_many: int):
    count = []
    while how_many > 0:
        password = uuid.uuid4()
        hash_key = hashlib.md5(str(password).encode() + salt.encode()).hexdigest()
        to_str = str(hash_key)
        cut_str = to_str
        if cut_str not in count:
            count.append(cut_str)
            how_many -= 1
        return cut_str
