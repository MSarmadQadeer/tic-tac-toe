condition = "y"
# ------This 'while loop' is for asking user that whether he wanna play again or not------
while condition == "y":
    print("YOU ARE GOING TO PLAY ------TIC TAC TOE------\n")
    name = input("Dear User..! Please Enter Your Name: ").upper()
    print("\nDear ", name, " ...! Best of Luck")
    # ------These variables are initialized for storing values of the Game(tic tac toe)------
    a = b = c = d = f = g = h = i = " "
    # ------This is the first computer move------
    print("\nComputer moves First\n")
    e = "O"
    print("      ", a, "|", b, "|", c, end="            ")
    print(1, "|", 2, "|", 3)
    print("      ", "---------", end="            ")
    print("---------")
    print("      ", d, "|", e, "|", f, end="            ")
    print(4, "|", 5, "|", 6)
    print("      ", "---------", end="            ")
    print("---------")
    print("      ", g, "|", h, "|", i, end="            ")
    print(7, "|", 8, "|", 9)
    # ------These variables are initialized for check purpose------
    m = n = o = p = q = r = s = t = " "
    loop = 1
    while loop < 5:
        user = input("\nDear User Enter Number 1-9: ")
        # ------The below 'if condition' is checking the valid data type------
        if user.isdigit():
            x = int(user)
            # ------This below 'if statement' is checking the available place in the game------
            if x == 5 or x == 0 or x == m or x == n or x == o or x == p or x == q or x == r or x == s or x == t or x > 9:
                print("\nThis Number Is Not Available...Please Enter A Valid Number")
                continue
            else:
                # ------These below statements are for User input------
                if x == 1:
                    a = "X"
                    m = 1
                if x == 2:
                    b = "X"
                    n = 2
                if x == 3:
                    c = "X"
                    o = 3
                if x == 4:
                    d = "X"
                    p = 4
                if x == 6:
                    f = "X"
                    q = 6
                if x == 7:
                    g = "X"
                    r = 7
                if x == 8:
                    h = "X"
                    s = 8
                if x == 9:
                    i = "X"
                    t = 9
                # ------These below statements are for computer input------
                if (b+c == "XX" or b+c == "OO" or d+g == "XX" or d+g == "OO" or e+i == "OO") and (a == " "):
                    a = "O"
                    m = 1
                elif (a+c == "XX" or a+c == "OO" or e+h == "OO") and (b == " "):
                    b = "O"
                    n = 2
                elif (a+b == "XX" or a+b == "OO" or f+i == "XX" or f+i == "OO" or g+e == "OO") and (c == " "):
                    c = "O"
                    o = 3
                elif (a+g == "XX" or a+g == "OO" or e+f == "OO") and (d == " "):
                    d = "O"
                    p = 4
                elif (c+i == "XX" or c+i == "OO" or d+e == "OO") and (f == " "):
                    f = "O"
                    q = 6
                elif (a+d == "XX" or a+d == "OO" or h+i == "XX" or h+i == "OO" or e+c == "OO" or a+h == "XX") and (g == " "):
                    g = "O"
                    r = 7
                elif (g+i == "XX" or g+i == "OO" or b+e == "OO") and (h == " "):
                    h = "O"
                    s = 8
                elif (g+h == "XX" or g+h == "OO" or f+c == "XX" or f+c == "OO" or a+e == "OO") and (i == " "):
                    i = "O"
                    t = 9
                else:
                    if a == " ":
                        a = "O"
                        m = 1
                    elif b == " ":
                        b = "O"
                        n = 2
                    elif c == " ":
                        c = "O"
                        o = 3
                    elif d == " ":
                        d = "O"
                        p = 4
                    elif f == " ":
                        f = "O"
                        q = 6
                    elif g == " ":
                        g = "O"
                        r = 7
                    elif h == " ":
                        h = "O"
                        s = 8
                    elif i == " ":
                        i = "O"
                        t = 9
        else:
            print("\nPlease Enter A Valid Data Type")
            continue
        print("\n      ", a, "|", b, "|", c, end="            ")
        print(1, "|", 2, "|", 3)
        print("      ", "---------", end="            ")
        print("---------")
        print("      ", d, "|", e, "|", f, end="            ")
        print(4, "|", 5, "|", 6)
        print("      ", "---------", end="            ")
        print("---------")
        print("      ", g, "|", h, "|", i, end="            ")
        print(7, "|", 8, "|", 9)
        # ------These below conditions are checking the result for the game------
        if (a+d+g == "OOO") or (b+e+h == "OOO") or (c+f+i == "OOO") or (a+b+c == "OOO") or (d+e+f == "OOO") or (g+h+i == "OOO") or (a+e+i == "OOO") or (g+e+c == "OOO"):
            print("\nDear ", name,
                  " The ---COMPUTER WINS---Best of Luck for next time")
            break
        elif (a+d+g == "XXX") or (b+e+h == "XXX") or (c+f+i == "XXX") or (a+b+c == "XXX") or (d+e+f == "XXX") or (g+h+i == "XXX") or (a+e+i == "XXX") or (g+e+c == "XXX"):
            print("\nDear ", name, " ---CONGRATULATIONS---You win the Game ")
            break
        loop = loop+1
    else:
        print("\nGAME DRAW")
    condition = input("\nPress 'y' If You Want To Play Again: ").lower()
