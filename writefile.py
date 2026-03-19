txt= "Hello, I'm writing in a file"
filePath= "tkt.txt"

try:
    with open(filePath, "x") as file: #returns file object
        file.write(txt)
        print("File has been written!")

except FileExistsError:
    print("File already exists")

    #x for writing but shows error if file exists already

import json
test_results= {
    "A": 30,
    "B":20,
    "C":35
}
file_path= "tkt.json"

with open(file= file_path, mode= "w") as file :
    json.dump(test_results,file,indent=4)
    print(f"Json file at {file_path} was created!")

import csv
employees= [["Name","Age"],
            ["Kritartha",19],
            ["David", 90]]
file_path= "tkt.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer= csv.writer(file)
        for row in employees:
            writer.writerow(row)
            print(F"Csv file was created on {file_path}")
except FileExistsError:
    print("No worries!")