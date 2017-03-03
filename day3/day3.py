lines = open("input").readlines()

def check_sides(a, b, c):
    return a + b > c and b + c > a and a + c > b

def star1():
    possible = 0
    for a, b, c in ((int(astr), int(bstr), int(cstr)) for line in lines for astr, bstr, cstr in [line.split()]):
        possible += check_sides(a, b, c)
    print("count of possible star1", possible)
star1()

def star2():
    possible = 0
    for a3, b3, c3 in ((a.split(), b.split(), c.split()) for (a, b, c) in zip(lines[0::3], lines[1::3], lines[2::3])):
        for a, b, c in ((int(a3[col]), int(b3[col]), int(c3[col])) for col in range(0, 3)):
            possible += check_sides(a, b, c)
    print("count of possible star2", possible)
star2()