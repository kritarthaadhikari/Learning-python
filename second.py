#Indexing=accessing elements of a squence using [] (indexing operator)
#         [start: and end:step]
# starting index is inclusive just like a []
# ending index is exclusive just like a ()

# credit_num= "1234-5678-9012"
# print(credit_num[0])#1
# print(credit_num[0:4])#1234
# #print(credit_num[:4])#1234
# #print(credit_num[4:])#-5678-9012

# #negative index means the count starts from behind
# print(credit_num[::2])#step
# #13-6891

creditcard_num= "1234-5678-9012-3456"
last_num= creditcard_num[-4:]
print(f"XXXX-XXXX-XXXX-{last_num}")
creditcard_num= creditcard_num[::-1]
print(f"credit number backwards is {creditcard_num}")

#format specifiers= {value:flags} format a value based on what
#                   flags are inserted

price1=2321
price2=-90101
price3=12.34
print(f"Price 1=€{price1:.2f}") #2321.00
print(f"Price 2=€{price2:.2f}")
print(f"Price 3=€{price3:.2f}")

print(f"Price 1=€{price1:20}") #€---20--2321
print(f"Price 2=€{price2:020}")#€0000000-90101
print(f"Price 3=€{price3:2}")

print(f"Price 1=€{price1:>10}")#right justify
print(f"Price 2=€{price2:<10}")#left justify
print(f"Price 3=€{price3:^10}")#centred

price4=201019192901
print(f"Price 4 ={price4:+,.2f}")#combination of flags
#Three different flags

