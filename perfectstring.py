str= input("Enter a string")
subset= set()
add=""
count=list()
i=0
subset.append(str)
for st in str:
    subset.append(str[i]+str[len(str)-1])
    subset.append(st)
    i+=1
length= len(str)
for j in range(0,len(str)):
    for i in range(j,len(str)-1) :
        add+= str[i]
        subset.append(add)
    add=""
for st in subset:
    
print(subset)
# for st in str:
#     for i in range(0, len(str)):
#         if str[i]==st:
            


