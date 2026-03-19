txt= "Hello, I'm writing in a file"
filePath= "tkt.txt"

with open(filePath, "w") as file: #returns file object
    file.write(txt)
    print("File has been written!")