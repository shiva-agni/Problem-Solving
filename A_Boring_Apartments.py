# by prerna

T=int(input())   # taking input
for k in range(0,T):
    X=input()
    a=len(X)
    b=int((a*(a+1))/2)
    x=int(X[0])

    # conditions for checking the values..
    if(x==1):
        print(b)
    elif(x==2):
        print(b+10)
    elif(x==3):
        print(b+20)
    elif(x==4):
        print(b+30)
    elif(x==5):
        print(b+40)
    elif(x==6):
        print(b+50)
    elif(x==7):
        print(b+60)
    elif(x==8):
        print(b+70)
    elif(x==9):
        print(b+80)

