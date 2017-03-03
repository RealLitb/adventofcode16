import hashlib
from itertools import count

def md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()

def star1(doorid, zerolen, keylen):
    key = ""
    zeroes = "0" * zerolen
    for i in count():
        hash = md5(doorid + str(i))
        if hash.startswith(zeroes):
            key += hash[zerolen]
            if len(key) == keylen:
                break
    return key
print("key is", star1("reyedfim", 5, 8))

def star2(doorid, zerolen, keylen):
    key = [None] * keylen
    zeroes = "0" * zerolen
    alarm = keylen
    for i in count():
        hash = md5(doorid + str(i))
        if hash.startswith(zeroes):
            pos, char = hash[zerolen:zerolen+2]
            if not pos.isdigit():
                continue
            # apparently md5 hexdigest returns bytes(), not str()!
            # still casting for safety.. since the manual says that it returns "a string object"
            pos = int(pos)
            if pos >= keylen:
                continue
            if key[pos] is None:
                key[pos] = char
                alarm -= 1
                if alarm == 0:
                    break
    return "".join(key)
print("key is", star2("reyedfim", 5, 8))



