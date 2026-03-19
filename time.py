import time
x=int(input("Enter time in second"))
for y in reversed(range(1,x+1)):
    minutes=int(y/60)%60
    hours=int(y/3600)%24
    seconds=y%60
    days=int(y/86400)%30
    months=int(y/2592000)%365
    years=int(y/946080000)
    print(f"{years:02}:{months:02}:{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!")


