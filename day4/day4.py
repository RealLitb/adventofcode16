import re

lines=open("input").readlines()

def dissect(line):
    return re.findall(r"([a-z-]+)([0-9]+)\[([a-z]+)\]", line)[0]

def is_decoy(name, checksum):
    fdist = {c: name.count(c) for c in name if c.islower()}
    # python's sort is stable
    most_common = sorted(sorted(fdist.items(), key=(lambda item: item[0])), key=(lambda item: item[1]), reverse=True)
    cc_checksum = "".join([c for c, count in most_common[:5]])
    return checksum == cc_checksum

def star1():
    sum_sectorids = 0
    for line in lines:
        name, sector_id, checksum = dissect(line)
        sum_sectorids += int(sector_id) if not is_decoy(name, checksum) else 0
    print("sum of real room ids", sum_sectorids)

def rotate(c, n):
    if c == "-":
        return " "
    return chr(ord('a') + (((ord(c)-ord('a')) + n) % 26))

def star2():
    for name, sector_id, checksum in (dissect(line) for line in lines):
        if is_decoy(name, checksum):
            pass # continue # um, the northpole store *is* a decoy!
        name = "".join(rotate(c, int(sector_id)) for c in name)
        print ("name", name, "sector id", sector_id, "north pole?", "****" if "north" in name else "Nope")

star1()
star2()
