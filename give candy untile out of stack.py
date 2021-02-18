y=0
o=0
bal=25
stack=25
while (o<stack):
    y=int(input("enter the how much candy u want "))
    if o<stack:
        x=0
        while x != y & y < bal:
            print("candy")
            x+=1
            
    o=o+y
    bal=stack-o
    if bal>0:
        print("stack left",bal)
    else:
        x=0
        bal=bal+y
        while x != bal:
            print("candy")
            x+=1
        print(" out of stack")
