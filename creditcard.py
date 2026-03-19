# Python credit card validator program

# 1.Remove any '-' or ' '
# 2.Add all digits in the odd places from right to left
# 3.Double every second digit from right to left.
#   (If result is a two-digit number,
#    add the two-digit number together to get a single digit.)
# 4.Sum the totals of steps 2 & 3
# 5.If sum is divisible by 10, the credit card # is valid


#Step 1
creditcard_num= input("Enter your credit card number")
creditcard_num=creditcard_num.replace("-","")
creditcard_num=creditcard_num.replace(" ","")


odd_sum=0
even_sum=0
total=0

#Step 2
for x in creditcard_num[::-2]:
    odd_sum+=int(x)

#Step 3
for x in creditcard_num[1::2]:
    x=int(x)*2
    if x>=10:
        even_sum+=1+(x%10)
    else:
        even_sum+=x

#Step 4
total=even_sum+odd_sum

#Step 5
if total%10==0:
    print(f"{creditcard_num} is Valid")
else:
    print(f"{creditcard_num} is invalid")



    
    