#Python file detection
import os

file_path="text.txt"
# Relative = folder/test.txt
# Absolute = C:/Users/BroCode/Desktop/test.txt

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesnt exist")

#Let's say i put text file in another folder named stuff 
#the way i can write its directory is by foldername/file name
# stuff/text.txt

#Let's check absolute file_path

file_path2= "C:/Users/akrit/OneDrive/Desktop/python/futile/text.txt"
#python thinks backslash as a tab character so either double
#backslash is used or forward slash is used

if os.path.exists(file_path2):
    print(f"The location '{file_path2}' exists")
else:
    print("That location doesnt exist")

"""Lets try folder(directory) now"""
file_path3="C:/Users/akrit/OneDrive/Desktop/python/futile"
if os.path.exists(file_path3):
    print(f"The location '{file_path3}' exists")

    if os.path.isfile(file_path3):
        print("That is a file")
    elif os.path.isdir(file_path3):
        print("It is a directory")
    
else:
    print("That location doesnt exist")

# Python writing files (.txt, .json, .csv)
# "r"  : Read mode (default). Fails if file does NOT exist.
# "w"  : Write mode. Creates file or overwrites existing file.
# "x"  : Exclusive creation. Fails if file already exists (FileExistsError).
# "a"  : Append mode. Creates file if missing; writes at end if exists.

# "r+" : Read + Write. File must already exist.
# "w+" : Write + Read. Overwrites existing file or creates new one.
# "a+" : Append + Read. Creates file if missing; cursor starts at end.

# Text vs Binary versions:
# "t"  : Text mode (default).
# "b"  : Binary mode (use for images, audio, etc.).

# Combine them:
# "rb" : Read binary
# "wb" : Write binary (overwrite)
# "xb" : Exclusive binary creation
# "ab" : Append binary

# Examples:
# "rt" : Read text
# "wt" : Write text
# "r+b": Read/Write binary
# "a+b": Append/Read binary

# --------- .txt ---------
txt_data = "I like pizza!"

file_path = "C:\\Users\\akrit\\OneDrive\\Desktop\\output.txt"

# with open(file_path,"x") as file:
#         file.write(txt_data)
#         print(f"Txt file {file_path} has been created")
try:
    with open(file_path,"a") as file:
        file.write(txt_data+ "\n")
        print(f"Txt file {file_path} has been created")
        #To append in a new line "\n" + txt_data should be used

except FileExistsError:
    print("File already exists")

Employees= ["Mike","Joe","Dave","Chester","Rob","Brad"]
with open(file_path, "a")as file:
    for employee in Employees:
        file.write(employee+ "\n")
    print("Employees added")

#FileExistsError: to avoid error handling is done

#with open(file=file_path,mode="w") as file: 
#using keyword arguments

# --------- .json ---------

import json

employee = {
   "name": "Spongebob",
   "age": 30,
   "job": "Cook"
}
# Common useful parameters:
# indent     : Pretty-print JSON (e.g., indent=4).
# sort_keys  : Sort dictionary keys alphabetically (True/False).
# ensure_ascii : Escapes non-ASCII chars if True. Keep characters as-is with False.
# default    : Function to handle objects that aren't JSON serializable.

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4)
        #json.dump(obj, file object, indent=4)
        

    print(f"JSON file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file already exists!")


# --------- .csv---------
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)#Obj created
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
