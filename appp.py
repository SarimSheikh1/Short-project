import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created successfully.")
    except FileExistsError:        
        print(f"File Name {filename}: Already exists.")
        
    except Exception as E:
        print('An error occurred!')
        
def view_all_files():
    files = os.listdir()    
    if not files:
        print('No files found!')
    else:
        print('Files in directory!')
        for file in files:
            print(file)
            
def deleete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name {filename}: Deleted successfully.")
    except FileNotFoundError:
        print(f"File Name {filename}: Not found.")
    except Exception as E:
        print('An error occurred!')
            
            
def read_file(filename):       
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' :\n{content}") 
    except FileNotFoundError:
        print(f"File Name {filename}: doesn't exist.")
    except Exception as E:
        print('An error occurred!')
    