import re
lines = open("input").readlines()

def star1():
    # note: the hyper match assumes that [..] do not nest
    annotation_re = re.compile(r"((\w)(?!\2)(\w)\3\2)")
    annotation_hyper_re = re.compile(r"\[[^]]*((\w)(?!\2)(\w)\3\2)[^]]*\]")

    number_tls = 0
    for line in lines:
        if annotation_re.findall(line) and not annotation_hyper_re.findall(line):
            number_tls += 1
    print("number of TLS supporting IPs", number_tls)

def star2():
    def supports_ssl(line, hypernet_spans):
        for (hybl, hyel), (hybr, hyer) in zip(hypernet_spans[0:], hypernet_spans[1:]):
            outside = line[hyel:hybr]
            for a, b, c in zip(outside[0:], outside[1:], outside[2:]):
                if a == c and a != b and a.isalpha() and b.isalpha():
                    inverse = "".join([b, a, b])
                    for hypernet in hypernet_spans:
                        if inverse in line[hypernet[0]:hypernet[1]]:
                            return True
        return False

    number_ssl = 0
    hypernets_re = re.compile(r"(\[.*?\])")
    for line in lines:
        hypernet_spans = [(0, 0)] + [m.span() for m in hypernets_re.finditer(line)] + [(len(line), 0)]
        if supports_ssl(line, hypernet_spans):
            number_ssl += 1
    print("number of SSL supporting IPs", number_ssl)

star1()
star2()
