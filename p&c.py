while True:
    print("Welcome To Permutation & Combination")
    print("For Permutation Type P & for c for combination")
    a = input().upper()
    if  a=="P":
        while True:
            print("Welcome to Permutation")
            print("N = Total Number Of term")
            print("R = Number of Posible term")
            N = int(input("Toatal Number Of Term : "))
            while True:
                r = int(input("Posible Number Of Term : "))
                if r <= N:
                    break
                else :
                    print("R Shoulb be <= N")   
            R = N-r
            n1 = 1
            for i in range(1,(N+1)):
                n1*=i
            #print("N term ",n1)
            r1 = 1
            for x in range(1,(R+1)):
                r1*=x
            #print("N-R term  ",r1)
            NpR = n1//r1
            print("N p R = ",NpR)
            print("Do You Wannt To Quit Permutatio ")
            print("Y/N")
            exit = input().upper()
            if exit == "Y":
                print("Thank's For Using Permutation")
                break

    elif a=="C":
        while True:
            print("Welcome To Combination")
            #print("N = Total Number Of term")
            #print("R = Number of Posible term")
            N = int(input("Toatal Number Of Term : "))
            while True:
                r = int(input("Posible Number Of Term : "))
                if r <= N:
                    break
                else :
                    print("R Shoulb be <= N")   
            R = N-r
            n1 = 1
            for i in range(1,(N+1)):
                n1*=i
            #print("N term ",n1)
            r1 = 1
            for x in range(1,(R+1)):
                r1*=x
            #print("N-R term  ",r1)
            R2 = 1
            for y in range(1,(r+1)):
                R2*=y
            #print("R term  ",R2)
            NcR = n1//(r1*R2)
            print("N c R = ",NcR)
            print("Do You Wannt To Quit Combination's ")
            print("Y/N")
            exit = input().upper()
            if exit == "Y":
                print("Thank's For Using Combination's")
                break
    else:
        print("Plz Enter A Walid Input")
        pass    
