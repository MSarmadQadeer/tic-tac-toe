print(1, "|", 2, "|", 3)
print("---------")
print(4, "|", 5, "|", 6)
print("---------")
print(7, "|", 8, "|", 9)
# First Computer Input
print("COMPUTER GOES FIRST")
a = b = c = d = f = g = h = i = " "
e = "O"
print(a, "|", b, "|", c)
print("---------")
print(d, "|", e, "|", f)
print("---------")
print(g, "|", h, "|", i)
# First User Input
x = int(input("Dear User Enter Number 1-9 :"))
a = "X" if x == 1 else a
b = "X" if x == 2 else b
c = "X" if x == 3 else c
d = "X" if x == 4 else d
f = "X" if x == 6 else f
g = "X" if x == 7 else g
h = "X" if x == 8 else h
i = "X" if x == 9 else i
# 2nd Computer Input
a = "O" if e+i == "OX" else a
b = "O" if e+h == "OX" else b
c = "O" if e+g == "OX" else c
d = "O" if e+f == "OX" else d
f = "O" if e+d == "OX" else f
g = "O" if e+c == "OX" else g
h = "O" if e+b == "OX" else h
i = "O" if e+a == "OX" else i
print(a, "|", b, "|", c)
print("---------")
print(d, "|", e, "|", f)
print("---------")
print(g, "|", h, "|", i)
# 2nd User Input
y = int(input("Dear User Enter Number 1-9 :"))
a = "X" if y == 1 else a
b = "X" if y == 2 else b
c = "X" if y == 3 else c
d = "X" if y == 4 else d
f = "X" if y == 6 else f
g = "X" if y == 7 else g
h = "X" if y == 8 else h
i = "X" if y == 9 else i
# 3rd Computer Input
if ((b+c == "XX") or (d+g == "XX") or (e+i == "OO")) and (a == " "):
    a = "O"
elif ((a+c == "XX") or (e+h == "OO")) and (b == " "):
    b = "O"
elif ((a+b == "XX") or (f+i == "XX") or (g+e == "OO")) and (c == " "):
    c = "O"
elif ((a+g == "XX") or (e+f == "OO")) and (d == " "):
    d = "O"
elif ((c+i == "XX") or (d+e == "OO")) and (f == " "):
    f = "O"
elif ((a+d == "XX") or (h+i == "XX") or (e+c == "OO")) and (g == " "):
    g = "O"
elif ((g+i == "XX") or (b+e == "OO")) and (h == " "):
    h = "O"
elif ((g+h == "XX") or (f+c == "XX") or (a+e == "OO")) and (i == " "):
    i = "O"
else:
    if a == " ":
        a = "O"
    elif b == " ":
        b = "O"
    elif c == " ":
        c = "O"
    elif d == " ":
        d = "O"
    elif f == " ":
        f = "O"
    elif g == " ":
        g = "O"
    elif h == " ":
        h = "O"
    elif i == " ":
        i = "O"
print(a, "|", b, "|", c)
print("---------")
print(d, "|", e, "|", f)
print("---------")
print(g, "|", h, "|", i)
# 3rd User Input
z = int(input("Dear User Enter Number 1-9 :"))
a = "X" if z == 1 else a
b = "X" if z == 2 else b
c = "X" if z == 3 else c
d = "X" if z == 4 else d
f = "X" if z == 6 else f
g = "X" if z == 7 else g
h = "X" if z == 8 else h
i = "X" if z == 9 else i
# 4th Computer Input
if ((b+c == "XX") or (d+g == "XX") or (e+i == "OO")) and (a == " "):
    a = "O"
elif ((a+c == "XX") or (e+h == "OO")) and (b == " "):
    b = "O"
elif ((a+b == "XX") or (f+i == "XX") or (g+e == "OO")) and (c == " "):
    c = "O"
elif ((a+g == "XX") or (e+f == "OO")) and (d == " "):
    d = "O"
elif ((c+i == "XX") or (d+e == "OO")) and (f == " "):
    f = "O"
elif ((a+d == "XX") or (h+i == "XX") or (e+c == "OO")) and (g == " "):
    g = "O"
elif ((g+i == "XX") or (b+e == "OO")) and (h == " "):
    h = "O"
elif ((g+h == "XX") or (f+c == "XX") or (a+e == "OO")) and (i == " "):
    i = "O"
else:
    if a == " ":
        a = "O"
    elif b == " ":
        b = "O"
    elif c == " ":
        c = "O"
    elif d == " ":
        d = "O"
    elif f == " ":
        f = "O"
    elif g == " ":
        g = "O"
    elif h == " ":
        h = "O"
    elif i == " ":
        i = "O"
print(a, "|", b, "|", c)
print("---------")
print(d, "|", e, "|", f)
print("---------")
print(g, "|", h, "|", i)
if (a+d+g == "OOO") or (b+e+h == "OOO") or (c+f+i == "OOO") or (a+b+c == "OOO") or (d+e+f == "OOO") or (g+h+i == "OOO") or (a+e+i == "OOO") or (g+e+c == "OOO"):
    print("COMPUTER WINS")
elif (a+d+g == "XXX") or (b+e+h == "XXX") or (c+f+i == "XXX") or (a+b+c == "XXX") or (d+e+f == "XXX") or (g+h+i == "XXX") or (a+e+i == "XXX") or (g+e+c == "XXX"):
    print("USER WINS")
# 4th User Input---If The Match Still Not Completed
else:
    z = int(input("Dear User Enter Number 1-9 :"))
    a = "X" if z == 1 else a
    b = "X" if z == 2 else b
    c = "X" if z == 3 else c
    d = "X" if z == 4 else d
    f = "X" if z == 6 else f
    g = "X" if z == 7 else g
    h = "X" if z == 8 else h
    i = "X" if z == 9 else i
# 5th Computer Input
    if ((b+c == "XX") or (d+g == "XX") or (e+i == "OO")) and (a == " "):
        a = "O"
    elif ((a+c == "XX") or (e+h == "OO")) and (b == " "):
        b = "O"
    elif ((a+b == "XX") or (f+i == "XX") or (g+e == "OO")) and (c == " "):
        c = "O"
    elif ((a+g == "XX") or (e+f == "OO")) and (d == " "):
        d = "O"
    elif ((c+i == "XX") or (d+e == "OO")) and (f == " "):
        f = "O"
    elif ((a+d == "XX") or (h+i == "XX") or (e+c == "OO")) and (g == " "):
        g = "O"
    elif ((g+i == "XX") or (b+e == "OO")) and (h == " "):
        h = "O"
    elif ((g+h == "XX") or (f+c == "XX") or (a+e == "OO")) and (i == " "):
        i = "O"
    else:
        if a == " ":
            a = "O"
        elif b == " ":
            b = "O"
        elif c == " ":
            c = "O"
        elif d == " ":
            d = "O"
        elif f == " ":
            f = "O"
        elif g == " ":
            g = "O"
        elif h == " ":
            h = "O"
        elif i == " ":
            i = "O"
    print(a, "|", b, "|", c)
    print("---------")
    print(d, "|", e, "|", f)
    print("---------")
    print(g, "|", h, "|", i)
    if (a+d+g == "OOO") or (b+e+h == "OOO") or (c+f+i == "OOO") or (a+b+c == "OOO") or (d+e+f == "OOO") or (g+h+i == "OOO") or (a+e+i == "OOO") or (g+e+c == "OOO"):
        print("COMPUTER WINS")
    elif (a+d+g == "XXX") or (b+e+h == "XXX") or (c+f+i == "XXX") or (a+b+c == "XXX") or (d+e+f == "XXX") or (g+h+i == "XXX") or (a+e+i == "XXX") or (g+e+c == "XXX"):
        print("USER WINS")
    else:
        print("GAME DRAWS")
