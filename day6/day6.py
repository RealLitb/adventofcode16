lines = open("input").readlines()

def star0(fn):
    freq_dist={}
    for line in lines:
        for i, c in enumerate(line):
            chars = freq_dist.setdefault(i, {})
            chars[c] = chars.get(c, 0) + 1

    for i in range(0, 8):
        print(fn(freq_dist[i].items(), key = (lambda item: item[1]))[0], end = "")
    print()

star0(max) # star 1
star0(min) # star 2

