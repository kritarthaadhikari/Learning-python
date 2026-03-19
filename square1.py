def module(testCase):
    count=0
    running= True
    while(running):
        a= int(input("Enter the length a"))
        b= int(input("Enter the length b"))
        c= int(input("Enter the length c"))
        d= int(input("Enter the length d"))
        if (a>0 and b>0 and c>0 and d>0):
            if(a<=10 and b<=10 and c<=10 and d<=10):
                count+=1
                if a==b==c==d:
                    print("YES")
                    
                else:
                    print("NO")
                    
            else:
                continue
    
        if count>testCase-1:
            running= False

isRun= True
while (isRun):
    testCase= int(input("Enter the no. of test cases"))
    if 0< testCase <= 10**4:
        module(testCase)
        isRun= False
    else:
        print("Invalid test Case")



