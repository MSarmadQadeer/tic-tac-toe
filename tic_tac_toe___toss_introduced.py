import random
condition="y"
while condition=="y":
    choice_store=[[" "," "," "],[" "," "," "],[" "," "," "]]
    slot_display=[[1,2,3],[4,5,6],[7,8,9]]
    m=n=o=p=q=r=s=t=u=" "
    #Below line of code decides the first turn between user and computer--------------------------------------------------------------------------------------------
    toss=random.randint(1,2)
    if toss==1:
        print("\nToss is Initialized And Computer Goes First\n")
        #Below lines of code are for random computer input ...if computer goes first--------------------------------------------------------------------------------
        x=random.randint(1,9)
        if x==1:
            choice_store[0][0]="O"
            slot_display[0][0]="-"
            m=1
        if x==2:
            choice_store[0][1]="O"
            slot_display[0][1]="-"
            n=2
        if x==3:
            choice_store[0][2]="O"
            slot_display[0][2]="-"
            o=3
        if x==4:
            choice_store[1][0]="O"
            slot_display[1][0]="-"
            p=4
        if x==5:
            choice_store[1][1]="O"
            slot_display[1][1]="-"
            q=5
        if x==6:
            choice_store[1][2]="O"
            slot_display[1][2]="-"
            r=6
        if x==7:
            choice_store[2][0]="O"
            slot_display[2][0]="-"
            s=7
        if x==8:
            choice_store[2][1]="O"
            slot_display[2][1]="-"
            t=8
        if x==9:
            choice_store[2][2]="O"
            slot_display[2][2]="-"
            u=9
    
    if toss==2:
        print("\nToss is Initialized And User Goes First\n")
    print( "      " ,choice_store[0][0], "|" ,choice_store[0][1], "|" ,choice_store[0][2], end="            ")
    print(slot_display[0][0], "|" ,slot_display[0][1], "|" ,slot_display[0][2])
    print("      " , "---------" , end="            ")
    print("---------")
    print( "      " ,choice_store[1][0], "|" ,choice_store[1][1], "|" ,choice_store[1][2], end="            ")
    print(slot_display[1][0], "|" ,slot_display[1][1], "|" ,slot_display[1][2])
    print("      " , "---------" , end="            ")
    print("---------")
    print( "      " ,choice_store[2][0], "|" ,choice_store[2][1], "|" ,choice_store[2][2], end="            ")
    print(slot_display[2][0], "|" ,slot_display[2][1], "|" ,slot_display[2][2])
    loop=1
    while loop<6:
        user=input("\nEnter Any Available Slot In Range 1-9: ")
        print()
        if user.isdigit():
            x=int(user)
            if x==0 or x>9 or x==m or x==n or x==o or x==p or x==q or x==r or x==s or x==t or x==u:
                print("\nPlease Enter The Available Slot\n")
                continue
        else:
            print("\nPlease Enter The Valid Data Type\n")
            continue
        #Below Lines of code are for User Input------------------------
        if x==1:
            choice_store[0][0]="X"
            slot_display[0][0]="-"
            m=1
        if x==2:
            choice_store[0][1]="X"
            slot_display[0][1]="-"
            n=2
        if x==3:
            choice_store[0][2]="X"
            slot_display[0][2]="-"
            o=3
        if x==4:
            choice_store[1][0]="X"
            slot_display[1][0]="-"
            p=4
        if x==5:
            choice_store[1][1]="X"
            slot_display[1][1]="-"
            q=5
        if x==6:
            choice_store[1][2]="X"
            slot_display[1][2]="-"
            r=6
        if x==7:
            choice_store[2][0]="X"
            slot_display[2][0]="-"
            s=7
        if x==8:
            choice_store[2][1]="X"
            slot_display[2][1]="-"
            t=8
        if x==9:
            choice_store[2][2]="X"
            slot_display[2][2]="-"
            u=9
        #Below Line Of Code Are For Computer Input-------------------------------------------------------------------------------------------------------------------------
        #1st Priority computer input-----------------------------------1---------------------------------------------------------------------------------------------------
        if (choice_store[0][1]+choice_store[0][2]=="OO" or choice_store[1][0]+choice_store[2][0]=="OO" or choice_store[1][1]+choice_store[2][2]=="OO") and (choice_store[0][0]==" "):
            choice_store[0][0]="O"
            slot_display[0][0]="-"
            m=1
        elif (choice_store[0][0]+choice_store[0][2]=="OO" or choice_store[1][1]+choice_store[2][1]=="OO") and (choice_store[0][1]==" "):
            choice_store[0][1]="O"
            slot_display[0][1]="-"
            n=2
        elif (choice_store[0][0]+choice_store[0][1]=="OO" or choice_store[1][2]+choice_store[2][2]=="OO" or choice_store[1][1]+choice_store[2][0]=="OO") and (choice_store[0][2]==" "):
            choice_store[0][2]="O"
            slot_display[0][2]="-"
            o=3
        elif (choice_store[0][0]+choice_store[2][0]=="OO" or choice_store[1][1]+choice_store[1][2]=="OO") and (choice_store[1][0]==" "):
            choice_store[1][0]="O"
            slot_display[1][0]="-"
            p=4
        elif (choice_store[0][0]+choice_store[2][2]=="OO" or choice_store[0][2]+choice_store[2][0]=="OO" or choice_store[0][1]+choice_store[2][1]=="OO" or choice_store[1][0]+choice_store[1][2]=="OO") and (choice_store[1][1]==" "):
            choice_store[1][1]="O"
            slot_display[1][1]="-"
            q=5
        elif (choice_store[1][0]+choice_store[1][1]=="OO" or choice_store[0][2]+choice_store[2][2]=="OO") and (choice_store[1][2]==" "):
            choice_store[1][2]="O"
            slot_display[1][2]="-"
            r=6
        elif (choice_store[0][0]+choice_store[1][0]=="OO" or choice_store[2][1]+choice_store[2][2]=="OO" or choice_store[1][1]+choice_store[0][2]=="OO") and (choice_store[2][0]==" "):
            choice_store[2][0]="O"
            slot_display[2][0]="-"
            s=7
        elif (choice_store[0][1]+choice_store[1][1]=="OO" or choice_store[2][0]+choice_store[2][2]=="OO") and (choice_store[2][1]==" "):
            choice_store[2][1]="O"
            slot_display[2][1]="-"
            t=8
        elif (choice_store[0][0]+choice_store[1][1]=="OO" or choice_store[2][1]+choice_store[2][0]=="OO" or choice_store[1][2]+choice_store[0][2]=="OO") and (choice_store[2][2]==" "):
            choice_store[2][2]="O"
            slot_display[2][2]="-"
            u=9
        #2nd Priority computer input-----------------------------------2-----------------------------------------------------------------------------------------------
        elif (choice_store[0][1]+choice_store[0][2]=="XX" or choice_store[1][0]+choice_store[2][0]=="XX" or choice_store[1][1]+choice_store[2][2]=="XX") and (choice_store[0][0]==" "):
            choice_store[0][0]="O"
            slot_display[0][0]="-"
            m=1
        elif (choice_store[0][0]+choice_store[0][2]=="XX" or choice_store[1][1]+choice_store[2][1]=="XX") and (choice_store[0][1]==" "):
            choice_store[0][1]="O"
            slot_display[0][1]="-"
            n=2
        elif (choice_store[0][0]+choice_store[0][1]=="XX" or choice_store[1][2]+choice_store[2][2]=="XX" or choice_store[1][1]+choice_store[2][0]=="XX") and (choice_store[0][2]==" "):
            choice_store[0][2]="O"
            slot_display[0][2]="-"
            o=3
        elif (choice_store[0][0]+choice_store[2][0]=="XX" or choice_store[1][1]+choice_store[1][2]=="XX") and (choice_store[1][0]==" "):
            choice_store[1][0]="O"
            slot_display[1][0]="-"
            p=4
        elif choice_store[1][1]==" ":
            choice_store[1][1]="O"
            slot_display[1][1]="-"
            q=5
        elif (choice_store[1][0]+choice_store[1][1]=="XX" or choice_store[0][2]+choice_store[2][2]=="XX") and (choice_store[1][2]==" "):
            choice_store[1][2]="O"
            slot_display[1][2]="-"
            r=6
        elif (choice_store[0][0]+choice_store[1][0]=="XX" or choice_store[2][1]+choice_store[2][2]=="XX" or choice_store[1][1]+choice_store[0][2]=="XX") and (choice_store[2][0]==" "):
            choice_store[2][0]="O"
            slot_display[2][0]="-"
            s=7
        elif (choice_store[0][1]+choice_store[1][1]=="XX" or choice_store[2][0]+choice_store[2][2]=="XX") and (choice_store[2][1]==" "):
            choice_store[2][1]="O"
            slot_display[2][1]="-"
            t=8
        elif (choice_store[0][0]+choice_store[1][1]=="XX" or choice_store[2][1]+choice_store[2][0]=="XX" or choice_store[1][2]+choice_store[0][2]=="XX") and (choice_store[2][2]==" "):
            choice_store[2][2]="O"
            slot_display[2][2]="-"
            u=9
        #To Avoid User Doubling---------------------------------------------------------------------------------------------------------------------------------------
        elif (choice_store[0][2]+choice_store[1][1]=="XX" or choice_store[1][1]+choice_store[2][0]=="XX" or choice_store[1][1]+choice_store[2][2]=="OX") and choice_store[0][0]==" ":
            choice_store[0][0]="O"
            slot_display[0][0]="-"
            m=1
        elif (choice_store[0][0]+choice_store[1][1]=="XX" or choice_store[1][1]+choice_store[2][2]=="XX" or choice_store[1][1]+choice_store[2][0]=="OX") and choice_store[0][2]==" ":
            choice_store[0][2]="O"
            slot_display[0][2]="-"
            o=3
        elif (choice_store[0][0]+choice_store[1][1]=="XX" or choice_store[1][1]+choice_store[2][2]=="XX" or choice_store[1][1]+choice_store[0][2]=="OX") and choice_store[2][0]==" ":
            choice_store[2][0]="O"
            slot_display[2][0]="-"
            s=7
        elif (choice_store[0][2]+choice_store[1][1]=="XX" or choice_store[1][1]+choice_store[2][0]=="XX" or choice_store[1][1]+choice_store[0][0]=="OX") and choice_store[2][2]==" ":
            choice_store[2][2]="O"
            slot_display[2][2]="-"
            u=9
              
        #3rd Priority computer input-----------------------------------3-----------------------------------------------------------------------------------------------
        #To Avoid User Doubling---------------------------------------------------------------------------------------------------------------------------------------
        elif (choice_store[0][1]+choice_store[2][0]=="XX" or choice_store[1][0]+choice_store[0][2]=="XX" or choice_store[0][1]+choice_store[1][0]=="XX") and (choice_store[0][0]==" "):
            choice_store[0][0]="O"
            slot_display[0][0]="-"
            m=1
        elif (choice_store[0][0]+choice_store[2][2]=="XX" or choice_store[2][0]+choice_store[0][2]=="XX") and (choice_store[0][1]==" "):
            choice_store[0][1]="O"
            slot_display[0][1]="-"
            n=2
        elif (choice_store[0][1]+choice_store[2][2]=="XX" or choice_store[0][0]+choice_store[1][2]=="XX" or choice_store[0][1]+choice_store[1][2]=="XX") and (choice_store[0][2]==" "):
            choice_store[0][2]="O"
            slot_display[0][2]="-"
            o=3
        elif (choice_store[0][0]+choice_store[2][2]=="XX" or choice_store[2][0]+choice_store[0][2]=="XX") and (choice_store[1][0]==" "):
            choice_store[1][0]="O"
            slot_display[1][0]="-"
            p=4
        elif (choice_store[0][0]+choice_store[2][2]=="XX" or choice_store[2][0]+choice_store[0][2]=="XX") and (choice_store[1][2]==" "):
            choice_store[1][2]="O"
            slot_display[1][2]="-"
            r=6
        elif (choice_store[0][0]+choice_store[2][1]=="XX" or choice_store[1][0]+choice_store[2][2]=="XX" or choice_store[1][0]+choice_store[2][1]=="XX") and (choice_store[2][0]==" "):
            choice_store[2][0]="O"
            slot_display[2][0]="-"
            s=7
        elif (choice_store[0][0]+choice_store[2][2]=="XX" or choice_store[2][0]+choice_store[0][2]=="XX") and (choice_store[2][1]==" "):
            choice_store[2][1]="O"
            slot_display[2][1]="-"
            t=8
        elif (choice_store[0][2]+choice_store[2][1]=="XX" or choice_store[1][2]+choice_store[2][0]=="XX" or choice_store[1][2]+choice_store[2][1]=="XX") and (choice_store[2][2]==" "):
            choice_store[2][2]="O"
            slot_display[2][2]="-"
            u=9
        #4th Priority Computer Input-----------------------------------4------------------------------------------------------------------------------------------------
        elif choice_store[1][1]=="X" and choice_store[0][0]==" " and choice_store[0][2]==" " and choice_store[2][0]==" " and choice_store[2][2]==" ":
            slots=[1,3,7,9]
            y=random.choice(slots)
            if y==1 and choice_store[0][0]==" ":
                choice_store[0][0]="O"
                slot_display[0][0]="-"
                m=1
            if y==3 and choice_store[0][2]==" ":
                choice_store[0][2]="O"
                slot_display[0][2]="-"
                o=3
            if y==7 and choice_store[2][0]==" ":
                choice_store[2][0]="O"
                slot_display[2][0]="-"
                s=7
            if y==9 and choice_store[2][2]==" ":
                choice_store[2][2]="O"
                slot_display[2][2]="-"
                u=9   
        #5th Priority computer input-----------------------------------5-----------------------------------------------------------------------------------------------
        else:
            if choice_store[0][0]==" ":
                choice_store[0][0]="O"
                slot_display[0][0]="-"
                m=1
            elif choice_store[0][1]==" ":
                choice_store[0][1]="O"
                slot_display[0][1]="-"
                n=2
            elif choice_store[0][2]==" ":
                choice_store[0][2]="O"
                slot_display[0][2]="-"
                o=3
            elif choice_store[1][0]==" ":
                choice_store[1][0]="O"
                slot_display[1][0]="-"
                p=4
            elif choice_store[1][1]==" ":
                choice_store[1][1]="O"
                slot_display[1][1]="-"
                q=5
            elif choice_store[1][2]==" ":
                choice_store[1][2]="O"
                slot_display[1][2]="-"
                r=6
            elif choice_store[2][0]==" ":
                choice_store[2][0]="O"
                slot_display[2][0]="-"
                s=7
            elif choice_store[2][1]==" ":
                choice_store[2][1]="O"
                slot_display[2][1]="-"
                t=8
            elif choice_store[2][2]==" ":
                choice_store[2][2]="O"
                slot_display[2][2]="-"
                u=9
        #----------------------------------------------------------------------------------------------------------------------------------------------------------
        print( "      " ,choice_store[0][0], "|" ,choice_store[0][1], "|" ,choice_store[0][2], end="            ")
        print(slot_display[0][0], "|" ,slot_display[0][1], "|" ,slot_display[0][2])
        print("      " , "---------" , end="            ")
        print("---------")
        print( "      " ,choice_store[1][0], "|" ,choice_store[1][1], "|" ,choice_store[1][2], end="            ")
        print(slot_display[1][0], "|" ,slot_display[1][1], "|" ,slot_display[1][2])
        print("      " , "---------" , end="            ")
        print("---------")
        print( "      " ,choice_store[2][0], "|" ,choice_store[2][1], "|" ,choice_store[2][2], end="            ")
        print(slot_display[2][0], "|" ,slot_display[2][1], "|" ,slot_display[2][2])
        loop=loop+1
        #Below lines of code are winning Conditions-------------------------------------------------------------------------------------------------------------------
        if (choice_store[0][0]+choice_store[0][1]+choice_store[0][2]=="OOO") or (choice_store[1][0]+choice_store[1][1]+choice_store[1][2]=="OOO")or(choice_store[2][0]+choice_store[2][1]+choice_store[2][2]=="OOO")or(choice_store[0][0]+choice_store[1][0]+choice_store[2][0]=="OOO")or(choice_store[0][1]+choice_store[1][1]+choice_store[2][1]=="OOO")or(choice_store[0][2]+choice_store[1][2]+choice_store[2][2]=="OOO")or(choice_store[0][0]+choice_store[1][1]+choice_store[2][2]=="OOO")or(choice_store[0][2]+choice_store[1][1]+choice_store[2][0]=="OOO"):
            print("\nDear User The ---COMPUTER WINS---Best of Luck for next time")
            break
        elif (choice_store[0][0]+choice_store[0][1]+choice_store[0][2]=="XXX") or (choice_store[1][0]+choice_store[1][1]+choice_store[1][2]=="XXX")or(choice_store[2][0]+choice_store[2][1]+choice_store[2][2]=="XXX")or(choice_store[0][0]+choice_store[1][0]+choice_store[2][0]=="XXX")or(choice_store[0][1]+choice_store[1][1]+choice_store[2][1]=="XXX")or(choice_store[0][2]+choice_store[1][2]+choice_store[2][2]=="XXX")or(choice_store[0][0]+choice_store[1][1]+choice_store[2][2]=="XXX")or(choice_store[0][2]+choice_store[1][1]+choice_store[2][0]=="XXX"):
            print("\nDear User ---CONGRATULATIONS---You win the Game ")
            break
        if slot_display[0][0]==slot_display[0][1]==slot_display[0][2]==slot_display[1][0]==slot_display[1][1]==slot_display[1][2]==slot_display[2][0]==slot_display[2][1]==slot_display[2][2]=="-":
            print("\nGAME DRAW")
            break
        
    condition=input("\nPress 'y' If You Want To Play Again: ").lower()
