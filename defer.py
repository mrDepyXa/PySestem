import os
import fnmatch
NoRoot = 'PySestem:/User/'
os.chdir(r'PySestem:/User/')

def full_file():
        for file in os.listdir('.'):
        	if fnmatch.fnmatch(file, '*.py'):
        		print(file)

def open_file():
	OpenenPut = input("Specify the location of the file:")
	OpenenFile = open(f"{NoRoot}{OpenenPut}")

def create_new_fille():
	os.create()

def delete_file():
	

def delete_pute():
	
