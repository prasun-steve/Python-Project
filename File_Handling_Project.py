from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")
    
    
def create_file():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to create: ")
        p = Path(name)
        if not p.exists():
            with open (p,'w') as fs:
                data = input("Enter the data to write in the file: ")
                fs.write(data)
            print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")
    except Exception as err:
        print(f"An error occurred: {err}")    

def read_file():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("Read Successfully")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"An error occurred: {err}")

def update_file():
    try:
        readfileandfolder()
        name=input("Enter the name of file to update:")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file:-")
            print("Press 2 for overwriting the data of your file:-")
            print("Press 3 for appending some content in your file:-")
            inp = int(input("Enter your Choice:"))
            if inp == 1:
                name2 = input("Give the new name of your file:")
                p2 = Path(name2)
                p.rename(p2)
                print(f"File renamed to '{name2}' successfully.")
            elif inp == 2:
                with open(p , "w") as fs:
                    data= input("Enter what you want to overwrite")
                    fs.write(data)
                    print("File Overwritten Successfully")
            elif inp == 3:
                with open(p , "a") as fs:
                    data = input("Enter the data you want to append:")
                    fs.write(" "+data)
                    print("File Appended Successfully")
    except Exception as err:
        print(f"An error occurred: {err}")


def delete_file():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to delete:")
        p = Path(name) 
        
        if p.exists() and p.is_file():
            os.remove(p)
            print("File Removed Successfully")
    except Exception as err:
        print(f"An error occurred: {err}")


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    create_file()

elif check == 2:
    read_file()

elif check == 3:
    update_file()
    
elif check == 4:
    delete_file()
